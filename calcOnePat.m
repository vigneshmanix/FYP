function [ outdata ] = calcOnePat( onepat )
%CALCONEPAT calculates heartrate and average blood pressure of one patient
%   Detailed explanation goes here
onepatECG = onepat(3,:);
[pks, locs] = findpeaks(onepatECG,'MinPeakProminence',max(onepatECG)/2);
heartrate = mean(diff(locs));

avgbp = mean(onepat(2,:));
outdata = cell2mat({heartrate  avgbp});

end

