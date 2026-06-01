from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
AI_COLOR = "#00bcd4"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Inteligencia Artificial", font_size=60, color=AI_COLOR).set_color_by_gradient(AI_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class MLScene(Scene):
    def construct(self):
        title = Text("Machine Learning", font_size=48, color=AI_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Regresion Lineal
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.3f}")
print(f"Coeficientes: {model.coef_}")

# Clasificacion - Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred))

# Clustering - K-Means
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Validacion cruzada
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"CV: {scores.mean():.3f} +/- {scores.std():.3f}")'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DeepScene(Scene):
    def construct(self):
        title = Text("Deep Learning", font_size=48, color=AI_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Red Neuronal con TensorFlow/Keras
import tensorflow as tf
from tensorflow import keras

# Perceptron Multicapa
model = keras.Sequential([
    keras.layers.Dense(128, activation="relu", input_shape=(784,)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Entrenamiento con callbacks
history = model.fit(
    X_train, y_train,
    batch_size=32,
    epochs=50,
    validation_split=0.2,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
        keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3),
        keras.callbacks.ModelCheckpoint("best_model.keras", save_best_only=True)
    ]
)

# CNN para clasificacion de imagenes
cnn = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class NLPScene(Scene):
    def construct(self):
        title = Text("Procesamiento del Lenguaje Natural", font_size=48, color=AI_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Tokenizacion con Hugging Face
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer(
    "Hola mundo, esto es NLP!",
    padding="max_length",
    truncation=True,
    max_length=128,
    return_tensors="pt"
)

# BERT para clasificacion
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)
outputs = model(**tokens)
predictions = outputs.logits.argmax(dim=-1)

# Word Embeddings con Word2Vec
from gensim.models import Word2Vec
sentences = [["hola", "mundo"], ["nlp", "es", "fascinante"]]
model_w2v = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
vector = model_w2v.wv["hola"]
similares = model_w2v.wv.most_similar("hola", topn=5)

# NLTK - Preprocesamiento de texto
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download("stopwords")
stemmer = SnowballStemmer("spanish")
tokens = ["corriendo", "corredor", "corre"]
raices = [stemmer.stem(t) for t in tokens]
# ["corr", "corredor", "corr"]

# GPT - Modelos de lenguaje
from openai import OpenAI
client = OpenAI()
respuesta = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Explica que es NLP"}]
)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class VisionScene(Scene):
    def construct(self):
        title = Text("Vision por Computadora", font_size=48, color=AI_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# OpenCV - Procesamiento de imagenes
import cv2
import numpy as np

# Cargar y preprocesar imagen
img = cv2.imread("imagen.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Deteccion de objetos con YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
outputs = net.forward(net.getUnconnectedOutLayersNames())

# Clasificacion con ResNet
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

resnet = ResNet50(weights="imagenet")
x = preprocess_input(img_array)
preds = resnet.predict(x)
resultados = decode_predictions(preds, top=3)[0]
for _, label, prob in resultados:
    print(f"{label}: {prob:.2%}")

# Segmentacion semantica
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
processor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

# Data Augmentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
    rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
    horizontal_flip=True, zoom_range=0.2, brightness_range=[0.8, 1.2]
)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class RLScene(Scene):
    def construct(self):
        title = Text("Agentes y Aprendizaje por Refuerzo", font_size=48, color=AI_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Q-Learning - Aprendizaje por Refuerzo
import numpy as np

# Inicializar Q-Table
q_table = np.zeros((num_estados, num_acciones))

# Hiperparametros
alpha = 0.1      # Tasa de aprendizaje
gamma = 0.95     # Factor de descuento
epsilon = 1.0    # Exploracion
epsilon_decay = 0.995
epsilon_min = 0.01

for episodio in range(1000):
    estado = entorno.reset()
    done = False
    total_reward = 0

    while not done:
        # Politica epsilon-greedy
        if np.random.random() < epsilon:
            accion = entorno.accion_muestral()
        else:
            accion = np.argmax(q_table[estado])

        nuevo_estado, reward, done = entorno.step(accion)

        # Actualizar Q-Table
        q_table[estado][accion] += alpha * (
            reward + gamma * np.max(q_table[nuevo_estado]) - q_table[estado][accion]
        )

        estado = nuevo_estado
        total_reward += reward

    epsilon = max(epsilon * epsilon_decay, epsilon_min)

print(f"Entrenamiento completado. Reward final: {total_reward}")

# Deep Q-Network (DQN)
# Red neuronal aproxima Q(s, a)
# Experiencia replay para estabilidad
# Target network para reducir correlacion'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Inteligencia Artificial", font_size=38, color=AI_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Regresion y clasificacion con scikit-learn", font_size=22, color=TEXT_COLOR),
            Text("Deep Learning con TensorFlow/Keras", font_size=22, color=TEXT_COLOR),
            Text("NLP con BERT y Transformers", font_size=22, color=TEXT_COLOR),
            Text("Vision por computadora con OpenCV", font_size=22, color=TEXT_COLOR),
            Text("Agentes y Q-Learning", font_size=22, color=TEXT_COLOR),
            Text("Redes neuronales convolucionales", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La tecnologia mas transformadora de nuestra era", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class InteligenciaArtificialFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        MLScene.construct(self)
        DeepScene.construct(self)
        NLPScene.construct(self)
        VisionScene.construct(self)
        RLScene.construct(self)
        ConclusionScene.construct(self)
