import json

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def process_data(piece):
    """
        python preprocess.py --num_workers 8 --name kks --in_dir .\datasets\kks --out_dir .\data\kks
        output : "./datasets/son/audio/NB10584578.0000.wav": "오늘부터 뉴스룸 2부에서는 그날의 주요사항을 한마디의 단어로 축약해서 앵커브리핑으로 풀어보겠습니다",
        input : 1/1_0000.wav|그는 괜찮은 척하려고 애쓰는 것 같았다.|그는 괜찮은 척하려고 애쓰는 것 같았다.|그는 괜찮은 척하려고 애쓰는 것 같았다.|3.5|He seemed to be pretending to be okay.
    """
    _content_path = "./datasets/kss/audio/" + piece.split("|")[0]
    _content = piece.split("|")[3]
    return _content_path, _content


def make_data_json():
    content_dict= dict()
    with open('./kss/transcript.v.1.4.txt') as f:
        for piece in read_in_chunks(f):
            path, content = process_data(piece)
            content_dict[path] = content
    print(content_dict)

    with open('./kss/kss-recognition-All.json', 'w',encoding = 'UTF-8') as fp:
        json.dump(content_dict, fp, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    make_data_json()