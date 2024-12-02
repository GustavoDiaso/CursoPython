def rotate_matrix(matrix: list):
    """
        This function is able to rotate a 3x3 matrix 90 degrees to the right 
    """
    try: 
        
        if (len(matrix[0]) * len(matrix)) == 9:
        
            # position '0:2' will be occupied by the original '0:0' element
            new_positions = {
                '0:2':'0:0',
                '2:2':'0:2',
                '2:0':'2:2',
                '0:0':'2:0',
                '1:2':'0:1',
                '2:1':'1:2',
                '1:0':'2:1',
                '0:1':'1:0',
                '1:1':'1:1'
            }

            new_matrix = [[], [], []]
        
        #   Putting the elements in their new position
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    current_position_element = matrix[int(new_positions[f'{i}:{j}'][0])][int(new_positions[f'{i}:{j}'][2])]
                    new_matrix[i].append(current_position_element)
                    
            print(new_matrix)
            
        else:
            raise Exception

    except:
        print("The argument passed was not valid.")



rotate_matrix([['A','B','C'], ['D', 'E', 'F'], ['G', 'H', 'I']])



