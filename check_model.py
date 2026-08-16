import joblib


model = joblib.load(
    "model/digital_distraction_final_model.pkl"
)


print("\n====================")
print("MODEL TYPE")
print("====================")

print(type(model))



print("\n====================")
print("MODEL CONTENT")
print("====================")


if isinstance(model,dict):

    print(
        model.keys()
    )


else:

    print(
        model
    )