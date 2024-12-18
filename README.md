The code is still being organized.

# CGSR
Repository for AAAI paper: Achieving Lightweight Super-resolution For Real-time Computer Graphics

# Overview


# Dataset Usage Instructions

The dataset is available at: https://kaggle.com/datasets/19684b7cee0ea0e51589d1a064446c2ac72e5167a3da9732f082463e2da84821

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
```

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

## Raw Data Processing

In the raw version of the feature files, there may be some edge information originating from the rendering process, which includes tiles. If you want to remove these extra edges and only retain the object boundaries, you can use the provided `dataenhance.py` script. Note: The algorithm is not yet perfect. We are actively working on optimizing it to achieve more accurate boundary cleaning and improved overall performance. Your feedback and suggestions are valuable as we continue to refine this process.

### Usage

The `dataenhance.py` script processes the feature files.  
It cleans up and retains only the object boundaries, removing unwanted edges present due to rendering tiles.

### Command Example

```bash
python dataenhance.py --input_path ./traces1/320/ --output_path ./traces1/320_clean/
```

# Acknowledgement
The models are built upon:

SRCNN: https://github.com/yjn870/SRCNN-pytorch

EDSR: https://github.com/sanghyun-son/EDSR-PyTorch

PAN: https://github.com/zhaohengyuan1/PAN

Our dataset is generated using a modified simulator from:

ATTILA-SIM: https://github.com/attila-gpu/attila-sim

# Citation
```
```

# License
MIT
