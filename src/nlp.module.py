def generate_alert(detections):
    if "NO-Hardhat" in detections:
        return "Worker without hardhat detected"
    elif "NO-Safety Vest" in detections:
        return "Worker without safety vest detected"
    elif "NO-Mask" in detections:
        return "Worker without mask detected"
    else:
        return "All workers compliant"