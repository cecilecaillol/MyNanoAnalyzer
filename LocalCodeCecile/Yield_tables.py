#!/usr/bin/env python
import ROOT
import re  
import argparse
from array import array


fileem2016pre=ROOT.TFile("datacard_emu_2016pre.root","r")
fileem2016post=ROOT.TFile("datacard_emu_2016post.root","r")
fileem2017=ROOT.TFile("datacard_emu_2017.root","r")
fileem2018=ROOT.TFile("datacard_emu_2018.root","r")

fileet2016pre=ROOT.TFile("datacard_etau_2016pre.root","r")
fileet2016post=ROOT.TFile("datacard_etau_2016post.root","r")
fileet2017=ROOT.TFile("datacard_etau_2017.root","r")
fileet2018=ROOT.TFile("datacard_etau_2018.root","r")

filemt2016pre=ROOT.TFile("datacard_mutau_2016pre.root","r")
filemt2016post=ROOT.TFile("datacard_mutau_2016post.root","r")
filemt2017=ROOT.TFile("datacard_mutau_2017.root","r")
filemt2018=ROOT.TFile("datacard_mutau_2018.root","r")

filett2016pre=ROOT.TFile("datacard_tautau_2016pre.root","r")
filett2016post=ROOT.TFile("datacard_tautau_2016post.root","r")
filett2017=ROOT.TFile("datacard_tautau_2017.root","r")
filett2018=ROOT.TFile("datacard_tautau_2018.root","r")

print("%em 0 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",fileem2016pre.Get("em_0").Get("ZTT").Integral()," & ",fileem2016post.Get("em_0").Get("ZTT").Integral()," & ",fileem2017.Get("em_0").Get("ZTT").Integral()," & ",fileem2018.Get("em_0").Get("ZTT").Integral(),"\\\\")
print("VV & ",fileem2016pre.Get("em_0").Get("VV").Integral()," & ",fileem2016post.Get("em_0").Get("VV").Integral()," & ",fileem2017.Get("em_0").Get("VV").Integral()," & ",fileem2018.Get("em_0").Get("VV").Integral(),"\\\\")
print("Fake & ",fileem2016pre.Get("em_0").Get("Fake").Integral()," & ",fileem2016post.Get("em_0").Get("Fake").Integral()," & ",fileem2017.Get("em_0").Get("Fake").Integral()," & ",fileem2018.Get("em_0").Get("Fake").Integral(),"\\\\")
print("signal & ",fileem2016pre.Get("em_0").Get("GGTT").Integral()," & ",fileem2016post.Get("em_0").Get("GGTT").Integral()," & ",fileem2017.Get("em_0").Get("GGTT").Integral()," & ",fileem2018.Get("em_0").Get("GGTT").Integral(),"\\\\")
print("Observed & ",fileem2016pre.Get("em_0").Get("data_obs").Integral()," & ",fileem2016post.Get("em_0").Get("data_obs").Integral()," & ",fileem2017.Get("em_0").Get("data_obs").Integral()," & ",fileem2018.Get("em_0").Get("data_obs").Integral(),"\\\\")

print("%em 1 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",fileem2016pre.Get("em_1").Get("ZTT").Integral()," & ",fileem2016post.Get("em_1").Get("ZTT").Integral()," & ",fileem2017.Get("em_1").Get("ZTT").Integral()," & ",fileem2018.Get("em_1").Get("ZTT").Integral(),"\\\\")
print("VV & ",fileem2016pre.Get("em_1").Get("VV").Integral()," & ",fileem2016post.Get("em_1").Get("VV").Integral()," & ",fileem2017.Get("em_1").Get("VV").Integral()," & ",fileem2018.Get("em_1").Get("VV").Integral(),"\\\\")
print("Fake & ",fileem2016pre.Get("em_1").Get("Fake").Integral()," & ",fileem2016post.Get("em_1").Get("Fake").Integral()," & ",fileem2017.Get("em_1").Get("Fake").Integral()," & ",fileem2018.Get("em_1").Get("Fake").Integral(),"\\\\")
print("signal & ",fileem2016pre.Get("em_1").Get("GGTT").Integral()," & ",fileem2016post.Get("em_1").Get("GGTT").Integral()," & ",fileem2017.Get("em_1").Get("GGTT").Integral()," & ",fileem2018.Get("em_1").Get("GGTT").Integral(),"\\\\")
print("Observed & ",fileem2016pre.Get("em_1").Get("data_obs").Integral()," & ",fileem2016post.Get("em_1").Get("data_obs").Integral()," & ",fileem2017.Get("em_1").Get("data_obs").Integral()," & ",fileem2018.Get("em_1").Get("data_obs").Integral(),"\\\\")

print("%et 0 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",fileet2016pre.Get("et_0").Get("ZTT").Integral()," & ",fileet2016post.Get("et_0").Get("ZTT").Integral()," & ",fileet2017.Get("et_0").Get("ZTT").Integral()," & ",fileet2018.Get("et_0").Get("ZTT").Integral(),"\\\\")
print("ZLL & ",fileet2016pre.Get("et_0").Get("ZLL").Integral()," & ",fileet2016post.Get("et_0").Get("ZLL").Integral()," & ",fileet2017.Get("et_0").Get("ZLL").Integral()," & ",fileet2018.Get("et_0").Get("ZLL").Integral(),"\\\\")
print("VV & ",fileet2016pre.Get("et_0").Get("VV").Integral()," & ",fileet2016post.Get("et_0").Get("VV").Integral()," & ",fileet2017.Get("et_0").Get("VV").Integral()," & ",fileet2018.Get("et_0").Get("VV").Integral(),"\\\\")
print("Fake & ",fileet2016pre.Get("et_0").Get("Fake").Integral()," & ",fileet2016post.Get("et_0").Get("Fake").Integral()," & ",fileet2017.Get("et_0").Get("Fake").Integral()," & ",fileet2018.Get("et_0").Get("Fake").Integral(),"\\\\")
print("signal & ",fileet2016pre.Get("et_0").Get("GGTT").Integral()," & ",fileet2016post.Get("et_0").Get("GGTT").Integral()," & ",fileet2017.Get("et_0").Get("GGTT").Integral()," & ",fileet2018.Get("et_0").Get("GGTT").Integral(),"\\\\")
print("Observed & ",fileet2016pre.Get("et_0").Get("data_obs").Integral()," & ",fileet2016post.Get("et_0").Get("data_obs").Integral()," & ",fileet2017.Get("et_0").Get("data_obs").Integral()," & ",fileet2018.Get("et_0").Get("data_obs").Integral(),"\\\\")

print("%et 1 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",fileet2016pre.Get("et_1").Get("ZTT").Integral()," & ",fileet2016post.Get("et_1").Get("ZTT").Integral()," & ",fileet2017.Get("et_1").Get("ZTT").Integral()," & ",fileet2018.Get("et_1").Get("ZTT").Integral(),"\\\\")
print("ZLL & ",fileet2016pre.Get("et_1").Get("ZLL").Integral()," & ",fileet2016post.Get("et_1").Get("ZLL").Integral()," & ",fileet2017.Get("et_1").Get("ZLL").Integral()," & ",fileet2018.Get("et_1").Get("ZLL").Integral(),"\\\\")
print("VV & ",fileet2016pre.Get("et_1").Get("VV").Integral()," & ",fileet2016post.Get("et_1").Get("VV").Integral()," & ",fileet2017.Get("et_1").Get("VV").Integral()," & ",fileet2018.Get("et_1").Get("VV").Integral(),"\\\\")
print("Fake & ",fileet2016pre.Get("et_1").Get("Fake").Integral()," & ",fileet2016post.Get("et_1").Get("Fake").Integral()," & ",fileet2017.Get("et_1").Get("Fake").Integral()," & ",fileet2018.Get("et_1").Get("Fake").Integral(),"\\\\")
print("signal & ",fileet2016pre.Get("et_1").Get("GGTT").Integral()," & ",fileet2016post.Get("et_1").Get("GGTT").Integral()," & ",fileet2017.Get("et_1").Get("GGTT").Integral()," & ",fileet2018.Get("et_1").Get("GGTT").Integral(),"\\\\")
print("Observed & ",fileet2016pre.Get("et_1").Get("data_obs").Integral()," & ",fileet2016post.Get("et_1").Get("data_obs").Integral()," & ",fileet2017.Get("et_1").Get("data_obs").Integral()," & ",fileet2018.Get("et_1").Get("data_obs").Integral(),"\\\\")

print("%mt 0 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",filemt2016pre.Get("mt_0").Get("ZTT").Integral()," & ",filemt2016post.Get("mt_0").Get("ZTT").Integral()," & ",filemt2017.Get("mt_0").Get("ZTT").Integral()," & ",filemt2018.Get("mt_0").Get("ZTT").Integral(),"\\\\")
print("ZLL & ",filemt2016pre.Get("mt_0").Get("ZLL").Integral()," & ",filemt2016post.Get("mt_0").Get("ZLL").Integral()," & ",filemt2017.Get("mt_0").Get("ZLL").Integral()," & ",filemt2018.Get("mt_0").Get("ZLL").Integral(),"\\\\")
print("VV & ",filemt2016pre.Get("mt_0").Get("VV").Integral()," & ",filemt2016post.Get("mt_0").Get("VV").Integral()," & ",filemt2017.Get("mt_0").Get("VV").Integral()," & ",filemt2018.Get("mt_0").Get("VV").Integral(),"\\\\")
print("Fake & ",filemt2016pre.Get("mt_0").Get("Fake").Integral()," & ",filemt2016post.Get("mt_0").Get("Fake").Integral()," & ",filemt2017.Get("mt_0").Get("Fake").Integral()," & ",filemt2018.Get("mt_0").Get("Fake").Integral(),"\\\\")
print("signal & ",filemt2016pre.Get("mt_0").Get("GGTT").Integral()," & ",filemt2016post.Get("mt_0").Get("GGTT").Integral()," & ",filemt2017.Get("mt_0").Get("GGTT").Integral()," & ",filemt2018.Get("mt_0").Get("GGTT").Integral(),"\\\\")
print("Observed & ",filemt2016pre.Get("mt_0").Get("data_obs").Integral()," & ",filemt2016post.Get("mt_0").Get("data_obs").Integral()," & ",filemt2017.Get("mt_0").Get("data_obs").Integral()," & ",filemt2018.Get("mt_0").Get("data_obs").Integral(),"\\\\")

print("%mt 1 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",filemt2016pre.Get("mt_1").Get("ZTT").Integral()," & ",filemt2016post.Get("mt_1").Get("ZTT").Integral()," & ",filemt2017.Get("mt_1").Get("ZTT").Integral()," & ",filemt2018.Get("mt_1").Get("ZTT").Integral(),"\\\\")
print("ZLL & ",filemt2016pre.Get("mt_1").Get("ZLL").Integral()," & ",filemt2016post.Get("mt_1").Get("ZLL").Integral()," & ",filemt2017.Get("mt_1").Get("ZLL").Integral()," & ",filemt2018.Get("mt_1").Get("ZLL").Integral(),"\\\\")
print("VV & ",filemt2016pre.Get("mt_1").Get("VV").Integral()," & ",filemt2016post.Get("mt_1").Get("VV").Integral()," & ",filemt2017.Get("mt_1").Get("VV").Integral()," & ",filemt2018.Get("mt_1").Get("VV").Integral(),"\\\\")
print("Fake & ",filemt2016pre.Get("mt_1").Get("Fake").Integral()," & ",filemt2016post.Get("mt_1").Get("Fake").Integral()," & ",filemt2017.Get("mt_1").Get("Fake").Integral()," & ",filemt2018.Get("mt_1").Get("Fake").Integral(),"\\\\")
print("signal & ",filemt2016pre.Get("mt_1").Get("GGTT").Integral()," & ",filemt2016post.Get("mt_1").Get("GGTT").Integral()," & ",filemt2017.Get("mt_1").Get("GGTT").Integral()," & ",filemt2018.Get("mt_1").Get("GGTT").Integral(),"\\\\")
print("Observed & ",filemt2016pre.Get("mt_1").Get("data_obs").Integral()," & ",filemt2016post.Get("mt_1").Get("data_obs").Integral()," & ",filemt2017.Get("mt_1").Get("data_obs").Integral()," & ",filemt2018.Get("mt_1").Get("data_obs").Integral(),"\\\\")

print("%tt 0 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",filett2016pre.Get("tt_0").Get("ZTT").Integral()," & ",filett2016post.Get("tt_0").Get("ZTT").Integral()," & ",filett2017.Get("tt_0").Get("ZTT").Integral()," & ",filett2018.Get("tt_0").Get("ZTT").Integral(),"\\\\")
print("VV & ",filett2016pre.Get("tt_0").Get("VV").Integral()," & ",filett2016post.Get("tt_0").Get("VV").Integral()," & ",filett2017.Get("tt_0").Get("VV").Integral()," & ",filett2018.Get("tt_0").Get("VV").Integral(),"\\\\")
print("Fake & ",filett2016pre.Get("tt_0").Get("Fake").Integral()," & ",filett2016post.Get("tt_0").Get("Fake").Integral()," & ",filett2017.Get("tt_0").Get("Fake").Integral()," & ",filett2018.Get("tt_0").Get("Fake").Integral(),"\\\\")
print("signal & ",filett2016pre.Get("tt_0").Get("GGTT").Integral()," & ",filett2016post.Get("tt_0").Get("GGTT").Integral()," & ",filett2017.Get("tt_0").Get("GGTT").Integral()," & ",filett2018.Get("tt_0").Get("GGTT").Integral(),"\\\\")
print("Observed & ",filett2016pre.Get("tt_0").Get("data_obs").Integral()," & ",filett2016post.Get("tt_0").Get("data_obs").Integral()," & ",filett2017.Get("tt_0").Get("data_obs").Integral()," & ",filett2018.Get("tt_0").Get("data_obs").Integral(),"\\\\")

print("%tt 1 track")
print(" & 2016 preVFP & 2016 postVFP & 2017 & 2018 \\\\")
print("\hline")
print("ZTT & ",filett2016pre.Get("tt_1").Get("ZTT").Integral()," & ",filett2016post.Get("tt_1").Get("ZTT").Integral()," & ",filett2017.Get("tt_1").Get("ZTT").Integral()," & ",filett2018.Get("tt_1").Get("ZTT").Integral(),"\\\\")
print("VV & ",filett2016pre.Get("tt_1").Get("VV").Integral()," & ",filett2016post.Get("tt_1").Get("VV").Integral()," & ",filett2017.Get("tt_1").Get("VV").Integral()," & ",filett2018.Get("tt_1").Get("VV").Integral(),"\\\\")
print("Fake & ",filett2016pre.Get("tt_1").Get("Fake").Integral()," & ",filett2016post.Get("tt_1").Get("Fake").Integral()," & ",filett2017.Get("tt_1").Get("Fake").Integral()," & ",filett2018.Get("tt_1").Get("Fake").Integral(),"\\\\")
print("signal & ",filett2016pre.Get("tt_1").Get("GGTT").Integral()," & ",filett2016post.Get("tt_1").Get("GGTT").Integral()," & ",filett2017.Get("tt_1").Get("GGTT").Integral()," & ",filett2018.Get("tt_1").Get("GGTT").Integral(),"\\\\")
print("Observed & ",filett2016pre.Get("tt_1").Get("data_obs").Integral()," & ",filett2016post.Get("tt_1").Get("data_obs").Integral()," & ",filett2017.Get("tt_1").Get("data_obs").Integral()," & ",filett2018.Get("tt_1").Get("data_obs").Integral(),"\\\\")
