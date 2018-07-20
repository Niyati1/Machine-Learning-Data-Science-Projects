import numpy as np
import csv

class Searcher:
    def __init__(self, indexPath):
        
        self.indexPath = indexPath

    # The search function search for visually similar micrographs, in the csv file where the histogram of all the micrographs are saved.
    # the limit here is 6, including the query micrograph, thus the result include query micrograph and the top 5 results for visually similar micrograph
    def search(self, queryFeatures, limit = 6):
        results = {}        
        with open(self.indexPath) as f:            
            reader = csv.reader(f)

            for row in reader:
                features = [float(x) for x in row[1:]]
                #the histograms are compared using euclidan squared distance
                d = self.euc_distance(features, queryFeatures)
                results[row[0]] = d
                f.close()

        results = sorted([(v, k) for (k, v) in results.items()])

        return results[:limit]

    def euc_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])

        return d