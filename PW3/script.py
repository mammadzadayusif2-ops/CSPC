#Task1
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt


df=pd.read_csv("Heart_disease_cleveland_new.csv")

print(df.describe())


print("Shape of the dataset:", df.shape)
print("First 5 rows of the dataset:","\n", df.head())
continuous=df[["age","chol","trestbps","thalach"]]

#Task2
fig,ax=plt.subplots(2,2,figsize=(12,10))

ax[0,0].hist(continuous["age"],bins=100)
ax[0,0].set_title("Age")

ax[0,1].hist(continuous["chol"],bins=100)
ax[0,1].set_title("Chol")

ax[1,0].hist(continuous["trestbps"],bins=100)
ax[1,0].set_title("Trestbps")

ax[1,1].hist(continuous["thalach"],bins=100)
ax[1,1].set_title("Thalach")

plt.savefig("heart_disease.png")
#plt.show()

#Task3
print("\n")
for column in continuous.columns:
    W,p=stats.shapiro(continuous[column])

    print(f"{column}: W={W}, p={p}")

    if p<0.05:
        print("Evidence against normality")
    else:
        print("Insufficient evidence against normality")

    print()


#Task4

tmean=df.groupby("target")["thalach"].mean()
print(tmean)

#Task5

tstd=df.groupby("target")["thalach"].std()
length=df.groupby("target")["thalach"].apply(lambda x: len(x))
ci1,ci2=tstd[0]/sqrt(length[0]),tstd[1]/sqrt(length[1])

for target in [0, 1]:
    mean=tmean[target]
    n=length[target]
    se = ci1 if target == 0 else ci2

    critical=stats.t.ppf(0.975, df=n-1)

    lower=mean-critical*se
    upper=mean+critical*se

    print(f"95% confidence interval: [{lower:.2f}, {upper:.2f}]")


groups = ["Healthy","Heart disease"]
means = [tmean[0], tmean[1]]

errors = [
    stats.t.ppf(0.975, df=length[0]-1)*ci1,
    stats.t.ppf(0.975, df=length[1]-1)*ci2
]

plt.figure(figsize=(7, 5))

plt.bar(groups, means)
plt.errorbar(groups, means,yerr=errors,fmt="none",ecolor="black", capsize=5)

plt.ylabel("Mean maximum heart rate (bpm)")
plt.title("Mean thalach with 95% confidence intervals")
plt.savefig("thalach_confidence_intervals.png")


#Task6
plt.figure()
x=df["age"]
y=df["thalach"]
plt.xlabel("Age")
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Age vs. Maximum Heart Rate")
plt.plot(x,y)
plt.savefig("age_thalach.png")


"""CANCER"""
print("\nCANCER DATASET:\n")
dfc=pd.read_csv("chemicals_cancer.csv")

r1,_=stats.pearsonr(dfc["benzene"],dfc["malignancy"])
r2,_=stats.pearsonr(dfc["cadmium"],dfc["malignancy"])

print("Corr between benzene and malignancy:",r1)
print("Corr between cadmium and malignancy:",r2)

dfc2=dfc[(dfc["pollution_index"]>40) & (dfc["pollution_index"]<60)] #& (dfc["age"]>30) & (dfc["age"]<50)]

r3,_=stats.pearsonr(dfc2["benzene"],dfc2["malignancy"])
r4,_=stats.pearsonr(dfc2["cadmium"],dfc2["malignancy"])

print("Corr between benzene and malignancy(After third variable):",r3)
print("Corr between cadmium and malignancy(After third variable):",r4)



#BONUS

print(df["target"].value_counts(normalize=True))





