# Dataset Usage Instructions

This dataset is organized into multiple `traces` directories, each containing data at various resolutions. Supported resolutions include `320`, `640`, `1280`, and `1600`. The dataset is provided as a compressed `.zip` file for ease of distribution. Detailed descriptions are provided below.

## Directory Structure

The dataset is structured as follows:
```plaintext
Dataset
│
├── traces1/
│   ├── 320/
│   │   ├── feature001.bmp
│   │   ├── frame001.sim.ppm
│   │   └── ...
│   ├── 640/
│   ├── 1280/
│   └── 1600/
│
├── traces2/
│   ├── 320/
│   ├── 640/
│   ├── 1280/
│   └── 1600/
│
└── ...

- Each `traces` directory corresponds to a unique trace.
- Subdirectories represent the resolution, with `320`, `640`, `1280`, and `1600` pixels being the supported sizes.
- Inside each resolution folder:
  - `feature+number.bmp` files store rendering information.
  - `frame+number.sim.ppm` files store corresponding simulation frame data.
- File naming conventions ensure pixel-level alignment between rendering information and frame data.

## File Naming Convention

- **Rendering Information**:
  - Stored in files named in the format: `feature+number.bmp`.
  - Example: `feature001.bmp`, `feature002.bmp`, etc.
  - Contains the encoded information in RGB channels.

- **Frame Files**:
  - Stored in files named in the format: `frame+number.sim.ppm`.
  - Example: `frame001.sim.ppm`, `frame002.sim.ppm`, etc.
  - Represents the raw simulation frame data.

- **Alignment**:
  - Each `feature+number.bmp` file corresponds to a `frame+number.sim.ppm` file.
  - The `number` in both filenames must match to ensure pixel-level alignment.

## Channel Description

- **R-channel**: Represents object edges.
  - Object edges are encoded as boolean values.
  - A pixel is marked as an edge pixel if it meets the specified edge criteria.

- **G-channel**: Encodes depth information.
  - Depth values are normalized to the range `[0, 1]`.

- **B-channel**: Contains normal vectors.
  - The values represent the angle of the normal vector relative to the camera.
  - The camera-facing direction (0 degrees) is mapped to `0`.
  - The side-facing direction (90 degrees) is mapped to `1`.
  - All values are normalized accordingly.
