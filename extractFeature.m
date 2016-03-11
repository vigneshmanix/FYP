load('Part_1.mat', 'Part_1')
td = cell2mat(cellfun(@calcOnePat,transpose(Part_1),'UniformOutput', false));
td(isnan(td)) = nanmedian(td(:,1));
csvwrite('FYPpreprocessed11mar2.csv',td);