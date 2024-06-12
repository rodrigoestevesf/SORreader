from traceOTDR import TraceOTDR

traco = TraceOTDR('arquivo1.sor')

# traco.getPoints()
# tracho.getDistances()
# tracho.getReflections()
traco.saveAsCSV()
traco.plotTrace()