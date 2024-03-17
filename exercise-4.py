def chunking_by(numbers, chunck):
    result = []

    # loop over the list, skipping each time by the chunck value
    for i in range(0, len(numbers), chunck):
        
        # set the starting and ending index of the chunck
        result_starting_index = i
        result_ending_index = i + chunck

        # create a list of numbers from the result_starting_index to the result_ending_index
        chunk_num = numbers[result_starting_index:result_ending_index]

        # append the chunk_num to the result list
        result.append(chunk_num)

    return result