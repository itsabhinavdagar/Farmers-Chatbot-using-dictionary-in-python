qna = {
    "hi":"Good to see you",
    "how are you":"I am cool",
    "nice to meet you":"How can i help you",
    "condition for cotton crop?":"It requires a lot of heat and plenty of sunshine.",
    "temperature for cotton?":"21-32 degree C temp. is required.",
    "climate for cotton?":"It prefers warm and humid climate.",
    "condition for wheat crop?":"It grows best in dry conditions.",
    "temperature for wheat?":"21-24 degree C warm temp. but not too hot. ",
    "climate for wheat?":"Area with low humidity.",
    "condition for potato crop?":"It is a rooting plant and requires light,loose, well-drained soil with a pH of 5.0 to 7.0.",
    "temperature for potato?":"18-24 degree C temp. is required.",
    "climate for potato?":"It grows best in cool, well-drained, loose soil & require 6 hrs. sunlight eachday for best.",
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])