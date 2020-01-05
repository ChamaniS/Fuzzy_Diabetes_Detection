
function val = evalFuzzy(Preg, Plas, Dias, Tric, Ins, Mass, Pedi, Age)
    fis = readfis('project.fis')
    val = evalfis([Preg, Plas, Dias, Tric, Ins, Mass, Pedi, Age], fis)
end