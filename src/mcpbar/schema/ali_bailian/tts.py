from enum import EnumMeta
from typing import Any, Union
from typing import AsyncGenerator, Generator, List, Union
import dataclasses

from dashscope.api_entities.dashscope_response import \
    MultiModalConversationResponse

class AlibailianTtsVoiceEnum(EnumMeta):
    Cherry = '芊悦'
    Serena = '苏瑶'
    Ethan = '晨煦'
    Chelsie = '千雪'
    Momo = '茉兔'
    Vivian = '十三'
    Moon = '月白'
    Maia = '四月'
    Kai = '凯'
    Nofish = '不吃鱼'
    Bella = '萌宝'
    Jennifer = '詹妮弗'
    Ryan = '甜茶'
    Katerina = '卡捷琳娜'
    Aiden = '艾登'
    Eldric_Sage = '沧明子'
    Mia = '乖小妹'
    Mochi = '沙小弥'
    Bellona = '燕铮莺'
    Vincent = '田叔'
    Bunny = '萌小姬'
    Neil = '阿闻'
    Elias = '墨讲师'
    Arthur = '徐大爷'
    Nini = '邻家妹妹'
    Ebona = '诡婆婆'
    Seren = '小婉'
    Pip = '顽屁小孩'
    Stella = '少女阿月'
    Bodega = '博德加'
    Sonrisa = '索尼莎'
    Alek = '阿列克'
    Dolce = '多尔切'
    Sohee = '素熙'
    Ono_Anna = '小野杏'
    Lenn = '莱恩'
    Emilien = '埃米尔安'
    Andre = '安德雷'
    Radio_Gol = '拉迪奥·戈尔'
    Jada = '上海-阿珍'
    Dylan = '北京-晓东'
    Li = '南京-老李'
    Marcus = '陕西-秦川'
    Roy = '闽南-阿杰'
    Peter = '天津-李彼得'
    Sunny = '四川-晴儿'
    Eric = '四川-程川'
    Rocky = '粤语-阿强'
    Kiki = '粤语-阿清'



class AlibailianTtsLanguageTypeEnum:
    """
    Chinese

    English

    German

    Italian

    Portuguese

    Spanish

    Japanese

    Korean

    French

    Russian
    """
    Chinese = 'Chinese'
    English = 'English'

@dataclasses.dataclass()
class AliBailianTtsRequestSchema:
    text: str
    voice: str
    language_type: str
    stream: bool


# class AliBailianTtsAudio:
#     data: str
#     url: str
#     id: str
#     expires_at: int
#
#
# class AliBailianTtsOutput:
#     text: str
#     finish_reason: str
#     choices: Any
#     audio: AliBailianTtsAudio
#
#
# class AliBailianTtsInputTokenDetails:
#     text_tokens: int
#
# class AliBailianTtsOutputTokenDetails:
#     text_tokens: int
#     audio_tokens: int
#
# class AliBailianTtsUsage:
#     input_tokens_details: AliBailianTtsInputTokenDetails
#     total_tokens: int
#     output_tokens: int
#     input_tokens: int
#     output_tokens_details: AliBailianTtsOutputTokenDetails
#     characters: int
#
# class AliBailianTtsResponseSchema:
#     status_code: int
#     request_id: str
#     code: str
#     message: str
#     output: AliBailianTtsOutput
#     usage: AliBailianTtsUsage


AliBailianTtsResponseSchema =  Union[MultiModalConversationResponse, Generator[
            MultiModalConversationResponse, None, None]]