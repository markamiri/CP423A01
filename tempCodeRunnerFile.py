for file_name in files[:2]:
    lowerize(file_name)
    tokenize(file_name)
    remove_stop_words(file_name)
    remove_special(file_name)
    remove_single(file_name)
    word_set = create_set(file_name)

    for word in word_set:
        word = str(word)
        if word in inverted_index:
            inverted_index[word].append(file_counter)
        else:
            inverted_index[word] = [file_counter]
    doc_id_name[file_counter] = file_name
    file_counter+=1