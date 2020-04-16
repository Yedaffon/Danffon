# coding=utf-8
# Copyright 2020 Yedaffon Author.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf
import numpy as np
import os

tf.enable_eager_execution()
# 读取文本, 验证字符长度是否合规:
text = open("shakespeare.txt", "rb").read().decode(encoding="utf-8")
print("文本字符长度: {} characters".format(len(text)))

vocabulary = sorted(set(text))

# One-Hot编码:
char2index = {w: k for k, w in enumerate(vocabulary)}
index2char = {k: w for k, w in enumerate(vocabulary)}

# text2array:
text2array = np.array([char2index[i] for i in text])

# 步长:
seq_length = 100
per_epoch = len(text) // seq_length

# 创建训练样本:
train_data = tf.data.Dataset.from_tensor_slices(text2array)

# 拼接数据:
sequences = train_data.batch(seq_length+1, drop_remainder=True)


# 制作训练集: 分为 input 和 target
def split_input_target(chunk):
    input_text = chunk[: -1]
    target_text = chunk[1:]
    return input_text, target_text


dataset = sequences.map(split_input_target)

# Batch_size:
BATCH_SIZE = 64
BUFFER_SIZE = 10000
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# 创建模型:
vocab_size = len(vocabulary)

# embedding维度
EMBEDDING_DIM = 256
RNN_UNITS = 1024


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                  batch_input_shape=[batch_size, None]),
        tf.keras.layers.GRU(rnn_units,
                            return_sequences=True,
                            stateful=True,
                            recurrent_initializer="glorot_uniform"),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model


def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)


model = build_model(
    vocab_size=vocab_size,
    embedding_dim=EMBEDDING_DIM,
    rnn_units=RNN_UNITS,
    batch_size=BATCH_SIZE
)


model.compile(optimizer="adam", loss=loss)

checkpoint_dir = "./training_checkpoints"

checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True
)

EPOCHS = 100

history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback], steps_per_epoch=1)

tf.train.latest_checkpoint(checkpoint_dir)

model = build_model(vocab_size, EMBEDDING_DIM, RNN_UNITS, batch_size=1)
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
model.build(tf.TensorShape([1, None]))

model.summary()


def generate_text(model, start_string):
    # 评估步骤(用学习过的模型生成文本)
    # 要生成的字符个数
    num_generate = 1000

    # 将起始字符串转换成数字(向量化)
    input_eval = [char2index[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # 空字符串用于存储结果
    text_generated = []

    # 低温生成更可预测的文本
    # 高温生成奇怪文本.
    temperature = 1.0

    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # 删除批次的维度
        predictions = tf.squeeze(predictions, 0)

        # 用分类分布预测模型返回的字符
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

        # 把预测字符和前面的隐藏状态一起传递给模型作为下一个输入
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(index2char[predicted_id])

    return start_string + ''.join(text_generated)


print(generate_text(model, start_string=u"ROMEO: "))
