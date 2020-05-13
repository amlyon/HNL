from CMGTools.HNL.update_deepflavour_base_cfg import process, cms
process.GlobalTag.globaltag = '102X_dataRun2_Prompt_v15' 
print '\nINFO: using GT', process.GlobalTag.globaltag, '\n\n'

##########################################################################################
## RERUN EGAMMA ID Fall17V2
##########################################################################################
# https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2
# from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
# setupEgammaPostRecoSeq(process,era='2018-Prompt')  
#a sequence egammaPostRecoSeq has now been created and should be added to your path, eg process.p=cms.Path(process.egammaPostRecoSeq)