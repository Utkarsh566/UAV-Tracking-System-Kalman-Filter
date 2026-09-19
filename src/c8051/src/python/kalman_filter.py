"""2D Kalman filter for noisy UAV position measurements."""

import numpy as np
import matplotlib.pyplot as plt


class Kalman2D:
    """Constant-velocity Kalman filter for x/y position."""

    def __init__(self, dt=1.0, process_noise=0.05, measurement_noise=4.0):
        self.F = np.array([[1,0,dt,0],
                           [0,1,0,dt],
                           [0,0,1,0],
                           [0,0,0,1]], dtype=float)
        self.H = np.array([[1,0,0,0],
                           [0,1,0,0]], dtype=float)
        self.Q = process_noise * np.eye(4)
        self.R = measurement_noise * np.eye(2)
        self.P = np.eye(4)
        self.x = np.zeros((4, 1))

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x.copy()

    def update(self, measurement):
        z = np.asarray(measurement, dtype=float).reshape(2, 1)
        innovation = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ innovation
        self.P = (np.eye(4) - K @ self.H) @ self.P
        return self.x.copy()


def demo_measurements():
    rng = np.random.default_rng(7)
    t = np.arange(60, dtype=float)
    true_x = 0.00008 * t + 0.000015 * t**2
    true_y = 0.00005 * t + 0.0008 * np.sin(t / 8.0)
    truth = np.column_stack((true_x, true_y))
    measurements = truth + rng.normal(0, 0.00008, truth.shape)
    return t, measurements, truth


def run_demo():
    _, measurements, truth = demo_measurements()
    kf = Kalman2D(process_noise=0.01, measurement_noise=1e-8)
    filtered = []

    for measurement in measurements:
        kf.predict()
        filtered.append(kf.update(measurement)[:2, 0])

    filtered = np.asarray(filtered)

    plt.figure(figsize=(8, 5))
    plt.plot(measurements[:, 0], measurements[:, 1], ".", label="Raw GPS")
    plt.plot(filtered[:, 0], filtered[:, 1], "-", label="Kalman filtered")
    plt.plot(truth[:, 0], truth[:, 1], "--", label="Reference trajectory")
    plt.xlabel("Position X")
    plt.ylabel("Position Y")
    plt.title("UAV Position Estimation using Kalman Filter")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/trajectory.png", dpi=180)
    plt.show()


if __name__ == "__main__":
    run_demo()
