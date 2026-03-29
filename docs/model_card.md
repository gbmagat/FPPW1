# Model Card – ASafeSight

## Model Details
- Model: YOLOv8 (Ultralytics)
- Task: PPE Detection (Object Detection)

## Dataset
- Source: Roboflow Construction Site Safety Dataset
- Size: ~700+ images
- Classes: Hardhat, Safety Vest, Mask, NO-Hardhat, etc.
- License: CC BY 4.0

## Metrics
- mAP@0.5: 0.92
- mAP@0.5–0.95: 0.736
- Precision: 0.88–0.89
- Recall: 0.87–0.95

## Intended Use
This model is designed to detect PPE compliance in construction environments.

## Limitations
- Limited dataset size
- Performance may drop in low lighting or occlusion
- Not suitable for real-time safety-critical decisions without supervision

## Ethical Considerations
- No facial recognition or identity tracking
- Used only for safety monitoring
- Should not be used for worker surveillance or punishment