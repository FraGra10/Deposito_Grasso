from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

TP = 12 #True positive
FP = 6  #False Positive
TN = 179 #True Negative
FN = 3  #False Negative
Precision_manuale = TP/(TP+FP)
Accuratezza_manuale = (TP+TN)/(TP + FP + TN + FN)
Recall_manuale = TP/(TP + FN)
F1_score_manuale = 2*Precision_manuale*Recall_manuale/(Precision_manuale+Recall_manuale)

y_vero     = [1]*15 + [0]*185
y_previsto = [1]*12 + [0]*3 + [1]*6 + 179*[0]

tn, fp, fn, tp = confusion_matrix(y_vero, y_previsto).ravel()   # ordine: TN, FP, FN, TP
print(confusion_matrix(y_vero, y_previsto))     # righe = reale, colonne = previsto
print(f"TP={tp} TN={tn} FP={fp} FN={fn}")

print("Accuratezza_manuale:", Accuratezza_manuale, "sklearn", accuracy_score(y_vero,y_previsto))
print("Precision manuale:", Precision_manuale , " sklearn:", precision_score(y_vero, y_previsto))
print("Recall manuale:   ", Recall_manuale , "  sklearn:", recall_score(y_vero, y_previsto))
print("F1_score manuale: ", F1_score_manuale, " sklearn:", f1_score(y_vero, y_previsto)  )