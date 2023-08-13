## Depth Estimation Model for Periocular Regions in VR

### Introduction

Amidst the growing concerns of eye strain and potential visual impairments associated with prolonged VR usage, the necessity for tools that can aid in understanding and alleviating these challenges is paramount. This depth estimation model specifically targets the periocular regions, offering researchers and developers a method to understand and quantify the depth-related aspects of this critical area.

### Model Overview

- **Architecture**: U-Net 3+ deep learning backbone.
- **Purpose**: Estimate measurable periocular depth maps.
- **Compatibility**: Designed to work seamlessly with any VR headset equipped with an eye-oriented monocular camera.

### Features

1. **High Precision**: Evaluated on a diverse sample set, the model demonstrated impressive accuracy in measuring random inter-mark-point distances around the eyes and assessing pupil diameter.
2. **Metric Basis**: Offers a foundation for protocols and guidelines related to light stimulus calculation and medical observations in VR.
3. **Integration with DPDG**: The model can be trained effectively using data synthesized from the Dynamic Periocular Data Generation (DPDG) environment.

### Getting Started

1. **Dependencies**: Python 3.11, Pytorch 2
2. **Usage**: Using jupyter notebook to open "model.ipynd", and follow the instraction to train the model.