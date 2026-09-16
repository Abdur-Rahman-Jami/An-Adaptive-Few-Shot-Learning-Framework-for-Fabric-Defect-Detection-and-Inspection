from pathlib import Path
import torch

project_root = Path('.').resolve()
workspace_roots = [project_root]
if project_root.parent != project_root:
    workspace_roots.append(project_root.parent)

print('workspace_roots:')
for p in workspace_roots:
    print(' -', p)

# find detector roots
print('\npattern detector roots:')
detector_roots = []
for root in workspace_roots:
    for name in ('Pattern_based_Anomaly_Detect', 'indiv anomaly detector'):
        candidate = root / name
        if candidate.exists():
            print(' -', candidate)
            detector_roots.append(candidate)

# list pattern keys (directory names)
keys = []
for dr in detector_roots:
    for child in sorted(dr.iterdir()):
        if child.is_dir():
            keys.append(child.name.strip().lower())
print('\npattern keys found:', keys)

# load pattern classifier checkpoint metadata (without building model)
ckpt_candidates = [project_root / 'Fabric_pattern_classifier' / 'best_efficientnet_fabric_print_woven.pth']
ckpt_path = None
for c in ckpt_candidates:
    if c.exists():
        ckpt_path = c
        break
print('\npattern classifier ckpt:', ckpt_path)
if ckpt_path:
    try:
        loaded = torch.load(ckpt_path, map_location='cpu')
        raw_labels = loaded.get('class_names') if isinstance(loaded, dict) else None
        print('pattern classifier class_names:', raw_labels)
    except Exception as e:
        print('failed to read pattern classifier ckpt:', e)

# show which pattern keys would match classifier labels
if ckpt_path and raw_labels:
    normalized = [l.strip().lower() for l in raw_labels]
    matches = []
    for lab in normalized:
        key = f"woven_{lab}"
        matches.append((lab, key, key in keys))
    print('\nclassifier label -> pattern key match:')
    for m in matches:
        print(' -', m)

print('\nDone')
