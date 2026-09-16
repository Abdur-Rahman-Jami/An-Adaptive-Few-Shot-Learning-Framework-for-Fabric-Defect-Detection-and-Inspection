from pathlib import Path
from app.ml_models import MLModelManager

m = MLModelManager(Path('.'))
print('workspace_roots:', [str(p) for p in m.workspace_roots])
print('pattern_detector_keys:', m._pattern_detector_keys())
print('pattern_anomaly_models keys:', list(m.pattern_anomaly_models.keys()))
print('pattern_labels (woven):', m.pattern_labels.get('woven'))
print('pattern_classifiers loaded for woven:', bool(m.pattern_classifiers.get('woven')))
for key in m._pattern_detector_keys():
    ckpt = m._resolve_pattern_anomaly_ckpt(key)
    print('pattern key', key, '-> ckpt:', ckpt)
print('woven proto ckpt:', m._resolve_woven_proto_ckpt())
print('woven proto support root:', m._resolve_woven_proto_support_root())
if m.woven_proto_classifier is None:
    print('woven_proto_classifier: None')
else:
    print('woven_proto_classifier class_names:', m.woven_proto_classifier.class_names)
