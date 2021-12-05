export TOKEN_LABEL=this_is_token_label
export PIN_SECRET=192837
export SO_PIN_SECRET=192837
softhsm2-util --init-token --slot 0 --label ${TOKEN_LABEL} --pin ${PIN_SECRET} --so-pin ${SO_PIN_SECRET}
