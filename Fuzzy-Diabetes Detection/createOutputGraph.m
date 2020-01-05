
function [] = createOutputGraph(x)
    fis = readfis('project.fis')
    h = figure;
    set(h, 'visible', 'off');
    set(h,'PaperUnits','inches','PaperPosition',[0 0 3 2])
    set(h,'DefaultTextFontSize', 14)
    plotmf(fis, 'output', 1)
    line([x, x], ylim, 'Color','b')
    saveas(h, 'output.jpg')
end