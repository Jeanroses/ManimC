from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
ML_COLOR = "#ff5722"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Machine Learning", font_size=60, color=ML_COLOR).set_color_by_gradient(ML_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class RegresionScene(Scene):
    def construct(self):
        title = Text("Regresion Lineal y Polinomial", font_size=48, color=ML_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Regresion Lineal Simple
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 6, 7, 8, 9])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print(f"Pendiente: {modelo.coef_[0]:.3f}")
print(f"Intercepto: {modelo.intercept_:.3f}")
print(f"R2 Score: {r2_score(y_test, modelo.predict(X_test)):.3f}")

# Regresion Polinomial
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=3)),
    ("linear", LinearRegression())
])

pipeline.fit(X_train, y_train)
print(f"R2 polinomial: {r2_score(y_test, pipeline.predict(X_test)):.3f}")

# Regularizacion
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

# Gradient Descent desde cero
def gradient_descent(X, y, lr=0.01, epochs=1000):
    m = len(y)
    w = np.zeros(X.shape[1])
    b = 0
    for _ in range(epochs):
        y_pred = X @ w + b
        dw = (2/m) * X.T @ (y_pred - y)
        db = (2/m) * np.sum(y_pred - y)
        w -= lr * dw
        b -= lr * db
    return w, b'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ClasifScene(Scene):
    def construct(self):
        title = Text("Clasificacion y Arboles", font_size=48, color=ML_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

clf = LogisticRegression(C=1.0, max_iter=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(confusion_matrix(y_test, y_pred))

# Decision Tree
from sklearn.tree import DecisionTreeClassifier, plot_tree

tree = DecisionTreeClassifier(max_depth=5, min_samples_split=10)
tree.fit(X_train, y_train)
print(f"Tree accuracy: {tree.score(X_test, y_test):.3f}")

# Random Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)
rf.fit(X_train, y_train)
print(f"RF accuracy: {rf.score(X_test, y_test):.3f}")
print(f"Feature importance: {rf.feature_importances_}")

# SVM - Support Vector Machine
from sklearn.svm import SVC

svm = SVC(kernel="rbf", C=1.0, gamma="scale")
svm.fit(X_train, y_train)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(X_train, y_train)

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(rf, X, y, cv=5)
print(f"CV scores: {scores.mean():.3f} +/- {scores.std():.3f}")'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ClusteringScene(Scene):
    def construct(self):
        title = Text("Clustering y Reduccion", font_size=48, color=ML_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# K-Means Clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Datos
X = np.random.randn(300, 2)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encontrar k optimo (Elbow Method)
inercias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inercias.append(kmeans.inertia_)

# K-Means con k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)
centroids = kmeans.cluster_centers_

# DBSCAN - Density-Based Clustering
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering

hier = AgglomerativeClustering(n_clusters=3, linkage="ward")
labels = hier.fit_predict(X_scaled)

# PCA - Principal Component Analysis
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f"Varianza explicada: {pca.explained_variance_ratio_}")
print(f"Total: {sum(pca.explained_variance_ratio_):.3f}")

# t-SNE - Visualizacion de alta dimension
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class PipelinesScene(Scene):
    def construct(self):
        title = Text("Pipelines y Preprocesamiento", font_size=48, color=ML_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Pipelines de scikit-learn
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    StandardScaler, OneHotEncoder, LabelEncoder
)
from sklearn.impute import SimpleImputer

# Preprocesamiento para datos mixtos
numeric_features = ["edad", "salario", "anos_experiencia"]
categorical_features = ["pais", "departamento", "rol"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(drop="first", sparse_output=False))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# Pipeline completo
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100))
])

# Grid Search con CV
from sklearn.model_selection import GridSearchCV

param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [5, 10, None],
    "classifier__min_samples_split": [2, 5, 10]
}

grid = GridSearchCV(
    pipeline, param_grid, cv=5,
    scoring="accuracy", n_jobs=-1
)
grid.fit(X_train, y_train)
print(f"Mejores params: {grid.best_params_}")
print(f"Mejor score: {grid.best_score_:.3f}")

# Feature Engineering
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DeepLearningScene(Scene):
    def construct(self):
        title = Text("Deep Learning con sklearn", font_size=48, color=ML_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Red Neuronal con MLP
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(
    hidden_layer_sizes=(100, 50),
    activation="relu",
    solver="adam",
    max_iter=500,
    learning_rate_init=0.001,
    early_stopping=True,
    validation_fraction=0.1
)
mlp.fit(X_train, y_train)
print(f"MLP accuracy: {mlp.score(X_test, y_test):.3f}")

# Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.8
)
gb.fit(X_train, y_train)

# XGBoost
import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
params = {
    "max_depth": 6,
    "eta": 0.1,
    "objective": "binary:logistic",
    "eval_metric": "logloss"
}
model = xgb.train(params, dtrain, num_boost_round=100)

# LightGBM
import lightgbm as lgb

lgb_train = lgb.Dataset(X_train, y_train)
params = {
    "boosting_type": "gbdt",
    "objective": "binary",
    "metric": "binary_logloss",
    "num_leaves": 31,
    "learning_rate": 0.05
}
gbm = lgb.train(params, lgb_train, num_boost_round=100)

# Guardar y cargar modelos
import joblib
joblib.dump(pipeline, "modelo.pkl")
pipeline_cargado = joblib.load("modelo.pkl")

# ONNX - Formato de intercambio
# skl2onnx: exportar sklearn a ONNX
# Se puede usar en cualquier runtime'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Machine Learning", font_size=38, color=ML_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Regresion lineal y polinomial", font_size=22, color=TEXT_COLOR),
            Text("Clasificacion con arboles y SVM", font_size=22, color=TEXT_COLOR),
            Text("Clustering: K-Means, DBSCAN", font_size=22, color=TEXT_COLOR),
            Text("PCA y reduccion de dimensionalidad", font_size=22, color=TEXT_COLOR),
            Text("Pipelines y Grid Search", font_size=22, color=TEXT_COLOR),
            Text("Gradient Boosting y XGBoost", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Algoritmos que aprenden de los datos", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class MachineLearningFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        RegresionScene.construct(self)
        ClasifScene.construct(self)
        ClusteringScene.construct(self)
        PipelinesScene.construct(self)
        DeepLearningScene.construct(self)
        ConclusionScene.construct(self)
