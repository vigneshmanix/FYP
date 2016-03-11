function [ outdata ] = calcOnePat( onepat )
%CALCONEPAT calculates heartrate and average blood pressure of one patient
%   onepat is one cell with three signal channels
%   onepatECG is the ECG signal
%   findpeaks finds local peaks and MinPeakProminence is set to half of max
%   locs has the location of the peak, pks has the peak value
%   The difference of locs will give distance between the peaks
%   We take mean over all the waves
%   The second channel has the blood pressure. avgbp is mean of blood pressure
onepatECG = onepat(3,:);
[pks, locs] = findpeaks(onepatECG,'MinPeakProminence',max(onepatECG)/2);
heartrate = mean(diff(locs));

avgbp = mean(onepat(2,:));
outdata = cell2mat({heartrate  avgbp});

end

