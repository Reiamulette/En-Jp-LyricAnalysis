import re


def adjustheader(file_content,filename, old_pattern):
    global extracted_header
    global bodycontent
    #find delimiter to mark the end of the header
    header_delimiter = file_content.find('*****')
    if header_delimiter != -1:
        extracted_header = file_content[:header_delimiter].strip()
        bodycontent = file_content[header_delimiter:].strip()

        # find where the old pattern to match is
        oldheader_matches = re.search(old_pattern, extracted_header, re.MULTILINE)

        if oldheader_matches:
            artist = oldheader_matches.group(1)
            song_title = oldheader_matches.group(2)
            year = oldheader_matches.group(3)
            category = oldheader_matches.group(4)

            new_header = f"Artist: {artist}\nSong Title: {song_title}\nYear: {year}\nCategory: {category}"
            # new_content = filename.replace(extracted_header, new_header)
            # Write the modified content back to the file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(new_header)
                file.write("\n*****")
                file.write(bodycontent)
                print(f"Old header '{extracted_header}' replaced with new formatted header in '{filename}'")

        else:
            pass



    else:
        extracted_header = ""
        print(f"No delimiter found in {filename}")


