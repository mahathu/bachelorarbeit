import sys, os, pickle

model_path = 'baked_models/'

if len(sys.argv) != 2:
    sys.stderr.write(f'Usage: python3 {sys.argv[0]} "Eingabetext"')

text = sys.argv[1]

with open(os.path.join(model_path, 'svr-22085815-20512769.est'), 'rb') as f:
    model_ZNS_GCS = pickle.load(f)
with open(os.path.join(model_path, 'svr-22085815-22086158.est'), 'rb') as f:
    model_ZNS_RASS = pickle.load(f)
with open(os.path.join(model_path, 'svr-22085836-20512769.est'), 'rb') as f:
    model_Pflege_GCS = pickle.load(f)
with open(os.path.join(model_path, 'svr-22085836-22086158.est'), 'rb') as f:
    model_Pflege_RASS = pickle.load(f)

print(f"""
Eingabetext interpretiert als Visite_ZNS:
RASS: {round(model_ZNS_RASS.predict([text])[0]):2} GCS: {round(model_ZNS_GCS.predict([text])[0]):2}
Eingabetext interpretiert als Visite_Pflege:
RASS: {round(model_Pflege_RASS.predict([text])[0]):2} GCS: {round(model_Pflege_GCS.predict([text])[0]):2}
""")