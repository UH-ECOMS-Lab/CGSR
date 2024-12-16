Dataset usage:
R-channel for object edges, G-channel for depth, and B-channel for normal vectors. 
For depth information, the values are normalized to a range of [0, 1]. 
For normal vectors, we map the camera-facing direction (0 degrees) to 0 and the side-facing direction (90 degrees) to 1, and then normalize the values accordingly. 
Object edges are represented using a boolean value, where a pixel is marked as an edge pixel if it meets the criteria.
