/*
 * Pyrogram - Telegram MTProto API Client Library for Python
 * Copyright (C) 2017-present Dan <https://github.com/delivrance>
 *
 * This file is part of Pyrogram.
 *
 * Pyrogram is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Pyrogram is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Modified by ohmyarthur <https://github.com/ohmyarthur>
 */

#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#ifndef AES256_H
#define AES256_H

#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
#define AES_INLINE static inline
#define AES_RESTRICT restrict
#else
#define AES_INLINE static
#define AES_RESTRICT
#endif

#define AES_BLOCK_SIZE 16
#define EXPANDED_KEY_SIZE 60

void aes256_set_encryption_key(const uint8_t key[AES_RESTRICT 32], uint32_t expandedKey[AES_RESTRICT 60]);
void aes256_set_decryption_key(const uint8_t key[AES_RESTRICT 32], uint32_t expandedKey[AES_RESTRICT 60]);
void aes256_encrypt(const uint8_t in[AES_RESTRICT 16], uint8_t out[AES_RESTRICT 16], const uint32_t expandedKey[AES_RESTRICT 60]);
void aes256_decrypt(const uint8_t in[AES_RESTRICT 16], uint8_t out[AES_RESTRICT 16], const uint32_t expandedKey[AES_RESTRICT 60]);

#endif
