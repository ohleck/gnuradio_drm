function [stream_out] = drm_ofdm(super_tframe, MSC, OFDM)
% calculates the complex baseband transmission signal

%% declare variables

N_S = OFDM.N_S;
r_max = OFDM.M_TF; % number of transmission frames in a super transmission frame

%% OFDM operation

nfft = OFDM.nfft;
nguard = OFDM.nguard;
%OFDM_signal = zeros(r_max * N_S, nfft + nguard);
OFDM_signal = zeros(1, r_max * N_S * (nfft + nguard));

for i = 1 : r_max * N_S
    %OFDM_signal(i, nguard + 1 : end) = ifft(super_tframe(:, i), nfft);
    OFDM_symbol = ifft(super_tframe(:, i), nfft);
    % insert guard interval
    OFDM_symbol_gi = [ OFDM_symbol(end - nguard + 1 : end); OFDM_symbol];
    %OFDM_signal(i, 1 : nguard) = OFDM_signal(i, end - nguard + 1 : end);
    OFDM_signal( (i-1)*(nfft + nguard) + 1 : i*(nfft + nguard)) = OFDM_symbol_gi;
end

stream_out = OFDM_signal;
end