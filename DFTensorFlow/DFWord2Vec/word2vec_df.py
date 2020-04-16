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

import word2vec

word2vec.word2phrase("text8", "text8-phrases", verbose=True)
word2vec.word2vec("text8-phrases", "text8.bin", size=100, verbose=True)
word2vec.word2clusters("text8", "text8-clusters.txt", 100, verbose=True)

model = word2vec.load("text8.bin")

print(model.vocab)

indexes, metrics = model.cosine("you")
output = model.generate_response(indexes, metrics).tolist()
print(output)
