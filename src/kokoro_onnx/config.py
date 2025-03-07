from pathlib import Path
from dataclasses import dataclass

MAX_PHONEME_LENGTH = 510
SAMPLE_RATE = 24000


@dataclass
class EspeakConfig:
    lib_path: str | None = None
    data_path: str | None = None


class KoKoroConfig:
    def __init__(
        self,
        model_path: str,
        voices_path: str,
        espeak_config: EspeakConfig | None = None,
    ):
        self.model_path = model_path
        self.voices_path = voices_path
        self.espeak_config = espeak_config

    def validate(self):
        if not Path(self.voices_path).exists():
            error_msg = f"Voices file not found at {self.voices_path}"
            error_msg += (
                "\nYou can download the voices file using the following command:"
            )
            error_msg += "\nwget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
            raise FileNotFoundError(error_msg)

        if not Path(self.model_path).exists():
            error_msg = f"Model file not found at {self.model_path}"
            error_msg += (
                "\nYou can download the model file using the following command:"
            )
            error_msg += "\nwget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx"
            raise FileNotFoundError(error_msg)


def get_vocab():
    _pad = "$"
    _punctuation = ';:,.!?¡¿—…"«»“” '
    _letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    _letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
    symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
    dicts = {}
    for i in range(len((symbols))):
        dicts[symbols[i]] = i
    return dicts


VOCAB = get_vocab()
