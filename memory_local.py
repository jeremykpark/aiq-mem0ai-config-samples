# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from aiq.builder.builder import Builder
from aiq.cli.register_workflow import register_memory
from aiq.data_models.memory import MemoryBaseConfig


class Mem0LocalMemoryClientConfig(MemoryBaseConfig, name="mem0_memory_local"):
    vec_store_provider: str = "qdrant"
    vec_store_collection_name: str = "test"
    vec_store_host: str = "localhost"
    vec_store_port: int = 6333
    embedding_model_dims: int = 768  # Change this according to your local model's dimensions
    llm_provider: str = "ollama"
    llm_model: str = "llama3.1:latest"
    llm_temperature: float = 0.0
    llm_max_tokens: int = 2000
    ollama_base_url: str = "http://localhost:11434"  # Ensure this URL is correct


@register_memory(config_type=Mem0LocalMemoryClientConfig)
async def mem0_memory_client(config: Mem0LocalMemoryClientConfig, builder: Builder):
    import os

    from mem0 import Memory

    from aiq.plugins.mem0ai.mem0_editor import Mem0Editor

    config = {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "collection_name": "test",
                "host": "localhost",
                "port": 6333,
                "embedding_model_dims": 768,  # Change this according to your local model's dimensions
            },
        },
        "llm": {
            "provider": "ollama",
            "config": {
                "model": "llama3.1:latest",
                "temperature": 0,
                "max_tokens": 2000,
                "ollama_base_url": "http://localhost:11434",  # Ensure this URL is correct
            },
        },
        "embedder": {
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text:latest",
                # Alternatively, you can use "snowflake-arctic-embed:latest"
                "ollama_base_url": "http://localhost:11434",
            },
        },
    }
    
    # Initialize Memory with the configuration
    mem0_client = Memory.from_config(config)

    memory_editor = Mem0Editor(mem0_client=mem0_client)

    yield memory_editor