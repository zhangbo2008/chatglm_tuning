from transformers import AutoTokenizer, AutoModel, TrainingArguments, AutoConfig
import torch
import torch.nn as nn
from peft import get_peft_model, LoraConfig, TaskType


class CastOutputToFloat(nn.Sequential):
    def forward(self, x): return super().forward(x).to(torch.float32)

na="THUDM/chatglm-6b"
model = AutoModel.from_pretrained(na, load_in_8bit=True, trust_remote_code=True, device_map='auto')
model.supports_gradient_checkpointing = True
model.gradient_checkpointing_enable()
model.enable_input_require_grads()
model.lm_head = CastOutputToFloat(model.lm_head)#等于多加了一层把输出变成32位的变化.因为这个模型一般是16字节的.
model.config.use_cache = False  # silence the warnings. Please re-enable for inference!