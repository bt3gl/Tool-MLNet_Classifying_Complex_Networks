
'''
This script add all the feature vectors into a big file

mari wahl @ 2014
'''


import os

FOLDERS_IN  = ['n2000', 'n1500', 'n3000']
SUBFILES = ['atlas', 'auto', 'carbon', 'cellular', 'citation','collaboration','communication', 'ground','location','meme','metabolic','products','road','signed','social','webgraphs','wiki','yeast']



if __name__ == '__main__':

    #final_file = open('all_nets.data', "w")
    final_file_together = open('all_neat.data', "w")

    for j in range(len(FOLDERS_IN)):        
        #final_file = open('all_nets_.data', "w")
        final_file = open('all_neat_' + FOLDERS_IN[j] + '.data', "w")

        # Loop into all the network folders
        for i in range(len(SUBFILES)):

            INPUT_PATH = 'vectors_neat/' + SUBFILES[i] + '_' +  FOLDERS_IN[j] + '.data'
            tempfile = open(INPUT_PATH)

            print 'Processing ' + INPUT_PATH 
            aux = tempfile.read()
            final_file.write(aux)
            final_file_together.write(aux)


    print '\nDone!!!'