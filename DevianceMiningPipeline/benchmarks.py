"""
This collects different ExperimentRunner instantiations to run experiments.
"""
import os
import shutil

from ExperimentRunner import ExperimentRunner
import sys
import os
from pathlib import Path


# def synth3():
#     INP_PATH = "logs/"
#     LOG_NAME = "synthetic3_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     results_folder = "synthetic3_results"
#     log_path_seq = "synthetic3_tagged_{}.xes"
#     results_file = "synthetic3_shorter_results.txt"
#
#     ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                           log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq, dt_max_depth=10,
#                           dt_min_leaf=5,
#                           experiment_name="synth3")
#
#     ex.prepare_cross_validation()
#     ex.prepare_data()
#     ex.train_and_eval_benchmark()
#
#
# def synth_mr1():
#     results_folder = "synth_mr"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_mr_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_mr_tagged_{}.xes"
#
#     results_file = "synth_mr_results_1.txt"
#
#     ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                           log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                           dt_min_leaf=5, dt_max_depth=10,
#                           experiment_name="mr1")
#
#     ex.prepare_cross_validation()
#     ex.prepare_data()
#     ex.train_and_eval_benchmark()
#
#
# def synth_tr1():
#     results_folder = "synth_tr"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_tr_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_tr_tagged_{}.xes"
#
#     results_file = "synth_tr_results_1.txt"
#
#     ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                           log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                           dt_min_leaf=5, dt_max_depth=10,
#                           experiment_name="tr1")
#
#     # ex.prepare_cross_validation()
#     # ex.prepare_data()
#     ex.train_and_eval_benchmark()
#
#
# def synth_tr1_coverage():
#     results_folder = "synth_tr"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_tr_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_tr_tagged_{}.xes"
#
#     results_file = "synth_tr_coverage_results_1.txt"
#
#     for i in (5, 15, 25):
#         ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=10, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               experiment_name="tr1_cov")
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#         # ex.prepare_cross_validation()
#         # ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
# def synth_mra1():
#     results_folder = "synth_mra"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_mra_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_mra_tagged_{}.xes"
#
#     results_file = "synth_pca_mra_results_1.txt"
#
#     ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                           log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                           dt_min_leaf=5, dt_max_depth=10, selection_method="fisher",
#                           experiment_name="mra")
#
#     # ex.prepare_cross_validation()
#     # ex.prepare_data()
#     ex.train_and_eval_benchmark()
#
#
# def synth_mra1_coverage():
#     results_folder = "synth_mra"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_mra_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_mra_tagged_{}.xes"
#
#     results_file = "synth_coverage_mra_results_1.txt"
#
#     for i in (5, 15, 25):
#         ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=10, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               experiment_name="mra1_coverage")
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#         # ex.prepare_cross_validation()
#         # ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
# def xray_coverage():
#     results_folder = "xray_results"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "merged_xray_fix.xes"
#     OUTPUTFOLDER = "xray/"
#     log_path_seq = "merged_xray_fix_{}.xes"
#
#     results_file = "xray_coverage_results.txt"
#
#     for i in (5, 15, 25):
#         ex = ExperimentRunner(output_file=results_file, results_folder=results_folder, inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=10, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               experiment_name="xray")
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#         # ex.prepare_cross_validation()
#         # ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
# def sepsis_er():
#     INP_PATH = "logs/"
#     EXP_NAME = "sepsis_er"
#     LOG_NAME = "mezelensen?.xes"
#     OUTPUTFOLDER = "Sepsis/"
#     results_folder = "sepsis_er_results"
#     log_path_seq = "sepsis_tagged_er_{}.xes"
#     results_file = "sepsis_er_coverage_results.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=3, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#            ex.prepare_cross_validation(0.2, "das")
#            ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()
#
#
# def sepsis_er_data():
#     INP_PATH = "logs/"
#     EXP_NAME = "sepsis_er"
#     LOG_NAME = "sepsis_tagged_er.xes"
#     OUTPUTFOLDER = "Sepsis/"
#     results_folder = "sepsis_er_results"
#     log_path_seq = "sepsis_tagged_er_{}.xes"
#     results_file = "sepsis_er_nodata.txt"
#     payload = False
#     payload_settings = "settings.cfg"
#
#     reencode = False
#
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=10, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               sequence_threshold=5, payload=payload, payload_settings=payload_settings,
#                               reencode=reencode)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()
# #
# #
# def sepsis_constraints():
#     INP_PATH = "logs/"
#     EXP_NAME = "sepsis_constraint"
#     LOG_NAME = "sepsis_constraint_tagged.xes"
#     OUTPUTFOLDER = "Sepsis/"
#     results_folder = "sepsis_constraint_results"
#     log_path_seq = "sepsis_constraint_tagged_{}.xes"
#     results_file = "sepsis_constraint_results.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#         #    ex.prepare_cross_validation()
#         #    ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()

# def bpi2012_accepted():
#     INP_PATH = "logs/"
#     EXP_NAME = "bpi2012_accepted"
#     LOG_NAME = "BPI_Challenge_2012_tagged_accepted.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2012_accepted_results"
#     log_path_seq = "BPI_Challenge_2012_tagged_accepted_{}.xes"
#     results_file = "BPI_Challenge_2012_tagged_accepted_results.txt"
#
#     selection_method = "coverage"
#     #selection_method = "rf_importance"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method=selection_method, coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
# def bpi2012_cancelled():
#     INP_PATH = "logs/"
#     EXP_NAME = "bpi2012_cancelled"
#     LOG_NAME = "BPI_Challenge_2012_tagged_cancelled.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2012_cancelled_results"
#     log_path_seq = "BPI_Challenge_2012_tagged_cancelled_{}.xes"
#     results_file = "BPI_Challenge_2012_tagged_cancelled_results.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#         #    ex.prepare_cross_validation()
#         #    ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
# def sepsis_sequence():
#     INP_PATH = "logs/"
#     EXP_NAME = "sepsis_sequence_2"
#     LOG_NAME = "sepsis_sequence_2_tagged.xes"
#     OUTPUTFOLDER = "Sepsis/"
#     results_folder = "sepsis_sequence_2_results"
#     log_path_seq = "sepsis_sequence_2_tagged_{}.xes"
#     results_file = "sepsis_csequence_2_results.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             #ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()
#
# def sig_disc_test():
#     INP_PATH = "logs/"
#     EXP_NAME = "test"
#     LOG_NAME = "multi.xes"
#     OUTPUTFOLDER = "Sepsis/"
#     results_folder = "multi_results"
#     log_path_seq = "multi_{}.xes"
#     results_file = "multi_results.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             #ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()


#
# def bpi2011_test():
#     INP_PATH = "logs/"
#     EXP_NAME = "test"
#     LOG_NAME = "multi.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2011_cc_res"
#     log_path_seq = "EnglishBPIChallenge2011_tagged_M13_{}.xes"
#     results_file = "2011_ripper_res.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()


# def bpi2011_data_cc():
#     INP_PATH = "logs/"
#     EXP_NAME = "test"
#     LOG_NAME = "EnglishBPIChallenge2011_tagged_cc_prep.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2011_cc_data_prep_res"
#     log_path_seq = "EnglishBPIChallenge2011_tagged_cc_prep_{}.xes"
#     results_file = "bpi2011_cc_data_prep_res.txt"
#     payload = True
#     payload_settings = "bpi2011_settings.cfg"
#     selection_method = "coverage"
#     #selection_method = "rf_importance"
#     #selection_method = "none"
#
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=5,
#                               selection_method=selection_method, coverage_threshold=i, sequence_threshold=5,
#                               payload=payload, payload_settings=payload_settings)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#         #    ex.prepare_cross_validation()
#         #    ex.prepare_data()
#         ex.train_and_eval_benchmark()

# ex.clean_data()
#
#
#
# def output_pos_neg_test():
#     INP_PATH = "logs/"
#     EXP_NAME = "output_pos_neg_data"
#     LOG_NAME = "output_pos_and_neg.xes"
#     OUTPUTFOLDER = "payload/"
#     results_folder = "output_pos_neg_res"
#     log_path_seq = "output_pos_and_neg_{}.xes"
#     results_file = "output_pos_neg.txt"
#
#     payload = True
#     payload_settings = "output_pos_and_neg_settings.cfg"
#
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=10,
#                               selection_method="coverage", coverage_threshold=i, sequence_threshold=5,
#                               payload=payload, payload_settings=payload_settings)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#         #    ex.prepare_cross_validation()
#         #    ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()
#
#
# def sepsis_er_dwd():
#
#
#     INP_PATH = "logs/"
#     EXP_NAME = "sepsis_er"
#     LOG_NAME = "sepsis_tagged_er.xes"
#     OUTPUTFOLDER = "SepsisDWD/"
#     results_folder = "sepsis_er_dwd_results"
#     log_path_seq = "sepsis_tagged_er_{}.xes"
#     results_file = "sepsis_results_data_5.txt"
#     payload_type = "normal" #dwd, normal or both
#
#     payload = True
#     payload_settings = "settings.cfg"
#     payload_dwd_settings = {
#         "ignored": ["Diagnosis",
#                     "Diagnose",
#                     "time:timestamp",
#                     "concept: name",
#                     "Label",
#                     "lifecycle: transition"
#     ]
#     }
#     reencode = False
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH,
#                               log_name=LOG_NAME, output_folder=OUTPUTFOLDER, log_template=log_path_seq,
#                               dt_max_depth=5, dt_min_leaf=5, selection_method="coverage", coverage_threshold=i,
#                               sequence_threshold=5, payload_type=payload_type, payload=payload, payload_settings=payload_settings,
#                               reencode=reencode, payload_dwd_settings=payload_dwd_settings)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#         #    #ex.prepare_cross_validation()
#         #    ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#
#
# def bpi2011_dwd_data_cc():
#     INP_PATH = "logs/"
#     EXP_NAME = "test"
#     LOG_NAME = "guada_indi2.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2011_dwd_results"
#     log_path_seq = "guada_indi2_{}.xes"
#     results_file = "bpi2011_results_fixed.txt"
#     payload = True
#     payload_settings = "bpi2011_settings.cfg"
#     selection_method = "coverage"
#
#     payload_type = "both" #dwd, normal or both
#     ignored = ["time:timestamp", "concept: name", "Label", "Start date", "End date", "Diagnosis", "Diagnosis code",
#                "Diagnosis Treatment", "Combination ID", "Treatment code", "Activity code"]
#
#     payload_dwd_settings = {
#         "ignored": ignored
#     }
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=5,
#                               selection_method=selection_method, coverage_threshold=i, sequence_threshold=5,
#                               payload=payload, payload_settings=payload_settings,
#                               payload_type=payload_type, payload_dwd_settings=payload_dwd_settings)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             ex.prepare_cross_validation(0.2)
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#
#     # ex.clean_data()
#
#
# def bpi2011_dwd_data_m16():
#     INP_PATH = "logs/"
#     EXP_NAME = "test"
#     LOG_NAME = "EnglishBPIChallenge2011_tagged_m16_prep.xes"
#     OUTPUTFOLDER = "EnglishBPI/"
#     results_folder = "bpi2011_t101_results"
#     log_path_seq = "EnglishBPIChallenge2011_tagged_m16_prep_{}.xes"
#     results_file = "bpi2011_t101_results.txt"
#     payload = True
#     payload_settings = "bpi2011_settings.cfg"
#     selection_method = "coverage"
#
#     payload_type = "normal" #dwd, normal or both
#     ignored = ["time:timestamp", "concept: name", "Label", "Start date", "End date", "Diagnosis", "Diagnosis code",
#                "Diagnosis Treatment", "Combination ID", "Treatment code", "Activity code"]
#
#     payload_dwd_settings = {
#         "ignored": ignored
#     }
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=5,
#                               selection_method=selection_method, coverage_threshold=i, sequence_threshold=5,
#                               payload=payload, payload_settings=payload_settings,
#                               payload_type=payload_type, payload_dwd_settings=payload_dwd_settings)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         #if nr == 0:
#             #ex.prepare_cross_validation()
#             #ex.prepare_data()
#         ex.train_and_eval_benchmark()

# ex.clean_data()

#
#
# def xray(split_perc="0.2", onlySplit=False, log_namee="", split_method="", features=None):
#
#     results_folder = "xray_results"
#
#     INP_PATH = "/home/sabuhi/Thesis/devianceminingthesis/DevianceMiningPipeline/logs/"
#     LOG_NAME = log_namee
#     OUTPUTFOLDER = "/home/sabuhi/Thesis/devianceminingthesis/DevianceMiningPipeline/xray/"
#     log_path_seq = log_namee[0:len(log_namee) - 4] + "_{}.xes"
#     EXP_NAME = "xray"
#     results_file = "xrayresults_new.txt"
#     payload = False
#     selection_method = "coverage"
#     ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                           inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                           payload=payload, log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=5,
#                           selection_method=selection_method, sequence_threshold=5)
#
#     try:
#         open("/home/sabuhi/Thesis/devianceminingthesis/DevianceMiningPipeline/logs/" + log_namee[0:len(log_namee) - 4] + "_1.xes")
#     except Exception:
#         ex.prepare_cross_validation(split_perc, split_method)
#
#     print("FINISHED only split ", onlySplit)
#     if onlySplit:
#         return
#     ex.prepare_data(features)
#
#     for nr, i in enumerate([5]):
#         ex.coverage_threshold = i
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#         ex.train_and_eval_benchmark(features)
#         # ex.clean_data()
from constants import cwd


def evaluate(
        split_perc="0.2",
        file_name="",
        payload_type=None,
        k_value=1,
        classifier=None,
        max_depth=None,
        min_samples=None,
        coverage_threshold=None
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
    ex.train_and_eval_benchmark()


# def synth_mr_new():
#     results_folder = "synth_mra_results"
#
#     EXP_NAME = "xray"
#     payload=False
#     selection_method = "coverage"
#
#     INP_PATH = "logs/"
#     LOG_NAME = "synth_mr_tagged.xes"
#     OUTPUTFOLDER = "Synthetic/"
#     log_path_seq = "synth_mr_tagged_{}.xes"
#
#     results_file = "synth_coverage_mr_results_1.txt"
#
#     for nr, i in enumerate((5, 15, 25)):
#         ex = ExperimentRunner(experiment_name=EXP_NAME, output_file=results_file, results_folder=results_folder,
#                               inp_path=INP_PATH, log_name=LOG_NAME, output_folder=OUTPUTFOLDER,
#                               payload=payload, log_template=log_path_seq, dt_max_depth=10, dt_min_leaf=5,
#                               selection_method=selection_method, coverage_threshold=i, sequence_threshold=5)
#
#         with open("train_" + results_file, "a+") as f:
#             f.write("\n")
#         with open("test_" + results_file, "a+") as f:
#             f.write("\n")
#
#         if nr == 0:
#             # ex.prepare_cross_validation()
#             ex.prepare_data()
#         ex.train_and_eval_benchmark()
#

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

    evaluate(
        split_perc,
        fileName,
        payload_type,
        k_value,
        classifier,
        max_depth,
        min_samples,
        coverage_threshold
    )

