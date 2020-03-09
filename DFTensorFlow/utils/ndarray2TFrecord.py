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

from typing import List
import tensorflow as tf


def ndarray2tfrecord(vectors: List[List[float]], labels: List[str], file: str):
    with tf.python_io.TFRecordWriter(file) as writer:
        for i in range(len(vectors)):
            features = tf.train.Features(
                feature={
                    "input_ids": tf.train.Feature(int64_list=tf.train.Int64List(value=[i])),
                    "input_data": tf.train.Feature(float_list=tf.train.FloatList(value=vectors[i])),
                    "input_label": tf.train.BytesList(bytes_list=tf.train.BytesList(
                        value=[labels[i].encode(encoding="utf-8")]))
                }
            )
            example = tf.train.Example(features=features)
            writer.write(example.SerializeToString())
