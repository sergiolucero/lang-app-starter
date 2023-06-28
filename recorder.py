import openai
import tiktoken
###############################
openai.api_key = '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'
COMPLETION_MODEL = "text-davinci-003"
TRANSCRIPTION_MODEL = "whisper-1"
TOP_TOKENS = 3800
AWS_COPY = 'aws s3 cp %s s3://cetram-estenio/FELIX/UPLOAD/'
