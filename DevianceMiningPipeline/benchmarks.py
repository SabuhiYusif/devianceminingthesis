"""
This collects different ExperimentRunner instantiations to run experiments.
"""
import shutil

from ExperimentRunner import ExperimentRunner
import sys
from pathlib import Path

from constants import cwd


def evaluate(
        split_perc="0.2",
        file_name="",
        payload_type=None,
        k_value=1,
        classifier=None,
        max_depth=None,
        min_samples=None,
        coverage_threshold=None,
        features=None
):
    results_folder = "xray_results"

    result_folder_path = Path(cwd + "/xray_results")

    if result_folder_path.exists():
        shutil.rmtree(result_folder_path)

    INP_PATH = cwd + "/logs/"
    LOG_NAME = file_name
    OUTPUTFOLDER = cwd + "/xray/"
    log_path_seq = file_name[0:len(file_name) - 4] + "_{}.xes"
    EXP_NAME = "xray"
    results_file = "xrayresults_new.txt"
    payload = False
    if payload_type == "normal" or payload_type == "both":
        payload = True
    payload_settings = "settings.cfg"
    selection_method = "coverage"
    ignored = ["time:timestamp", "concept: name", "Label", "Start date", "End date", "Diagnosis", "Diagnosis code",
               "Diagnosis Treatment", "Combination ID", "Treatment code", "Activity code"]

    payload_dwd_settings = {
        "ignored": ignored
    }

    ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
                          inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
                          payload=payload, log_template=log_path_seq, dt_max_depth=max_depth, dt_min_leaf=min_samples,
                          payload_settings=payload_settings, payload_type=payload_type,
                          payload_dwd_settings=payload_dwd_settings, selection_method=selection_method,
                          sequence_threshold=5, k_value=k_value, split_perc=split_perc,
                          classifier=classifier, max_depth=max_depth, min_samples=min_samples)

    ex.prepare_data()

    ex.coverage_threshold = coverage_threshold
    with open("train_" + results_file, "a+") as f:
        f.write("\n")
    with open("test_" + results_file, "a+") as f:
        f.write("\n")
    ex.train_and_eval_benchmark(features)

def read_XES_log(path):
    tic = time()

    print("Parsing log")
    with open(path) as log_file:
        log = XUniversalParser().parse(log_file)[0]  # take first log from file

    toc = time()

    print("Log parsed, took {} seconds..".format(toc - tic))

    return log


def str_to_bool(s):
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    else:
        raise ValueError


if __name__ == "__main__":
    sys_len = len(sys.argv)

    split_perc = sys.argv[1]
    fileName = sys.argv[2]
    payload_type = sys.argv[3]
    k_value = int(sys.argv[4])
    classifier = sys.argv[5]
    max_depth = int(sys.argv[6])
    min_samples = int(sys.argv[7])
    coverage_threshold = int(sys.argv[8])
    feature_sets = sys.argv[9]

    featureList = feature_sets.split(":")


    features = {
        "ia": True if featureList[0] == 'ia' else False,
        "declare": True if featureList[1] == 'declare' else False,
        "seq": True if featureList[2] == 'seq' else False,
        "hyb": True if featureList[3] == 'hyb' else False
    }


    evaluate(
        split_perc,
        fileName,
        payload_type,
        k_value,
        classifier,
        max_depth,
        min_samples,
        coverage_threshold,
        features
    )

