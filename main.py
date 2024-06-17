from traceOTDR import TraceOTDR

traco = TraceOTDR('arquivo2.sor')

# traco.getPoints()
# tracho.getDistances()
# tracho.getReflections()

print(traco.getNumberOfPoints())
traco.saveAsCSV()
traco.plotTrace()