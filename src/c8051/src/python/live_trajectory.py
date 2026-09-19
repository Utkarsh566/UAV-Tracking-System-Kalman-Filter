"""UAV trajectory visualization from demo or CSV data.

CSV format:
timestamp,latitude,longitude,distance_cm
"""

import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt
from kalman_filter import Kalman2D


def run_demo():
    rng = np.random.default_rng(10)
    t = np.arange(60, dtype=float)
    truth = np.column_stack((
        0.00008 * t + 0.000015 * t**2,
        0.00005 * t + 0.0008 * np.sin(t / 8.0)
    ))
    measurements = truth + rng.normal(0, 0.00008, truth.shape)

    kf = Kalman2D(process_noise=0.01, measurement_noise=1e-8)
    filtered = []

    for measurement in measurements:
        kf.predict()
        filtered.append(kf.update(measurement)[:2, 0])

    filtered = np.asarray(filtered)

    plt.figure(figsize=(8, 5))
    plt.plot(measurements[:, 0], measurements[:, 1], ".", label="Raw GPS")
    plt.plot(filtered[:, 0], filtered[:, 1], "-", label="Kalman filtered")
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("UAV Trajectory Demonstration")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/filtered_gps.png", dpi=180)
    plt.show()


def read_csv(filename):
    rows = []
    with open(filename, newline="") as file:
        for row in csv.DictReader(file):
            rows.append([float(row["latitude"]), float(row["longitude"])])
    return np.asarray(rows)


def plot_csv(filename):
    measurements = read_csv(filename)
    if len(measurements) == 0:
        raise ValueError("CSV contains no position measurements.")

    kf = Kalman2D(process_noise=0.01, measurement_noise=1e-8)
    filtered = []

    for measurement in measurements:
        kf.predict()
        filtered.append(kf.update(measurement)[:2, 0])

    filtered = np.asarray(filtered)

    plt.figure(figsize=(8, 5))
    plt.plot(measurements[:, 1], measurements[:, 0], ".", label="Raw GPS")
    plt.plot(filtered[:, 1], filtered[:, 0], "-", label="Kalman filtered")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("UAV GPS Trajectory")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/trajectory.png", dpi=180)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--csv")
    args = parser.parse_args()

    if args.demo:
        run_demo()
    elif args.csv:
        plot_csv(args.csv)
    else:
        parser.error("Use --demo or --csv FILE.")
