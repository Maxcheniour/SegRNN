#!/bin/bash

if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
model_name=SegRNN

root_path_name=./dataset/
data_path_name=weather_origin.csv
model_id_name=weather
data_name=custom

for pred_len in 96 192 336
do
    python -u run_longExp.py \
      --is_training 1 \
      --root_path $root_path_name \
      --data_path $data_path_name \
      --model_id $model_id_name'_'$seq_len'_'$pred_len \
      --model $model_name \
      --data $data_name \
      --features M \
      --seq_len 720 \
      --pred_len $pred_len \
      --seg_len 48 \
      --enc_in 21 \
      --d_model 512 \
      --dropout 0.5 \
      --train_epochs 30 \
      --target "Tpot (K)" \
      --patience 10 \
      --rnn_type gru \
      --dec_way pmf \
      --itr 1 --batch_size 64 --learning_rate 0.0001 > logs/LongForecasting/$model_name'_'$model_id_name'_'$seq_len'_'$pred_len.log
done