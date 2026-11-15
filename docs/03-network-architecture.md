# FibreTrace — Network Architecture

## 1. Introduction

This document explains the network architecture used in FibreTrace.

The network represents a simplified multi-provider internet connectivity environment. It contains two customer sites, two separate Fibre Network Operator (FNO) access domains, a shared Internet Service Provider (ISP), an Internet Exchange Point (IXP), an upstream transit provider and several network services.

The purpose of this architecture is to provide a controlled environment where different network failures can be introduced and investigated.

## 2. High-Level Network Topology

The network follows this logical structure:

```text
                         CUSTOMER SITE A
                         ┌───────────────┐
                         │     PC-A      │
                         │ 10.10.10.10  │
                         └───────┬───────┘
                                 │
                               SW-A
                                 │
                               CPE-A
                                 │
                               FNO-A
                                 │
                                 │
                         ┌───────▼───────┐
                         │   ISP-EDGE    │
                         └───────┬───────┘
                                 │
                         ┌───────▼───────┐
                         │   ISP-CORE    │
                         └───────┬───────┘
                                 │
                              CORE-SW
                         ┌───────┼────────┐
                         │       │        │
                      IXP-PEER TRANSIT-R DNS-SERVER
                         │       │
                      LOCAL-  GLOBAL-
                       WEB     WEB


                         CUSTOMER SITE B
                         ┌───────────────┐
                         │     PC-B      │
                         │ 10.20.20.10  │
                         └───────┬───────┘
                                 │
                               SW-B
                                 │
                               CPE-B
                                 │
                               FNO-B
                                 │
                                 └──── ISP-EDGE