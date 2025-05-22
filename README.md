# 🌿 HazelGrove Testing Repository

Welcome to the **Testing Repo for Project HazelGrove**. This repository serves as a sandbox for testing features, components, and workflows related to the main HazelGrove project.

---

## 🚧 Purpose

This repository is used to:

- Track bug fixes and prototype solutions
- Validate component behavior in isolation
- Test integration and deployment workflows

---

## 📁 Project Structure

```bash
hazelgrove-testing/
├── Accessibility-Testing/     # Accessibility Testing Suite  
├── Authentication-Testing/    # Authentication Testing Suite     
├── Performance-Testing/       # Performance Testing Suite     
├── Product-Management/        # Product Information Manager Testing Suite   
├── Search-Functionality/      # Search Bar Testing Suite   
├── Security-Testing/          # Security Testing Suite  
├── Store-Component/           # Store Component Testing Suite  
├── Supabase-Integration/      # Supabase Integration Testing Suite  
├── UI-Components/             # UI Components Testing Suite  
├── User-Management/           # User Management Testing Suite
├── expand.py                  # Test Suite Expansion CSV  
└── README.md                  # Project Documentation
```

## Up-to-Date Updates
[Project HazelGrove Test Plan](https://docs.google.com/spreadsheets/d/1D-2j-H0TQNjCP05YD2ctwywwGUVOJ1oXHSQjTot5Z-0/edit?gid=184807390#gid=184807390) <br/>
[Project Hazel Grove TCM](https://docs.google.com/spreadsheets/d/13fxEy2P3ricwzi8u7n2ufLLJyfDS4K6THt8URVaXO74/edit?gid=2078614767#gid=2078614767)

## 🧪 Test Cases

This section outlines the various test suites and individual test cases designed for Project HazelGrove. Each test case links to a detailed markdown file describing its purpose, steps, and expected outcomes.

*   [Authentication Testing](/Authentication-Testing)
    *   [AUTH-0001: Authentication - Email Validation](/Authentication-Testing/AUTH-0001_authentication_email_validation.md)
    *   [AUTH-0002: Authentication - Password Validation](/Authentication-Testing/AUTH-0002_authentication_password_validation.md)
    *   [AUTH-0003: Authentication - Injection Prevention](/Authentication-Testing/AUTH-0003_authentication_injection_prevention.md)
    *   [AUTH-0004: Authentication - Sign Up Flow](/Authentication-Testing/AUTH-0004_authentication_sign_up_flow.md)
    *   [AUTH-0005: Authentication - Sign In Flow](/Authentication-Testing/AUTH-0005_authentication_sign_in_flow.md)
    *   [AUTH-0006: Authentication - OAuth Integration](/Authentication-Testing/AUTH-0006_authentication_oauth_integration.md)
    *   [AUTH-0007: Authentication - Password Reset](/Authentication-Testing/AUTH-0007_authentication_password_reset.md)
    *   [AUTH-0008: Authentication - Rate Limiting](/Authentication-Testing/AUTH-0008_authentication_rate_limiting.md)
*   [Search Functionality](/Search-Functionality)
    *   [SEARCH-0001: Search - Product Search](/Search-Functionality/SEARCH-0001_search_product_search.md)
    *   [SEARCH-0002: Search - Store Search](/Search-Functionality/SEARCH-0002_search_store_search.md)
    *   [SEARCH-0003: Search - Combined Search](/Search-Functionality/SEARCH-0003_search_combined_search.md)
    *   [SEARCH-0004: Search - Short Term Handling](/Search-Functionality/SEARCH-0004_search_short_term_handling.md)
    *   [SEARCH-0005: Search - Empty Results Handling](/Search-Functionality/SEARCH-0005_search_empty_results_handling.md)
    *   [SEARCH-0006: Search - Store Selection](/Search-Functionality/SEARCH-0006_search_store_selection.md)
*   [Store Component](/Store-Component)
    *   [STORE-0001: Store - Data Loading](/Store-Component/STORE-0001_store_data_loading.md)
    *   [STORE-0002: Store - Real-time Updates](/Store-Component/STORE-0002_store_real_time_updates.md)
    *   [STORE-0003: Store - Pagination](/Store-Component/STORE-0003_store_pagination.md)
    *   [STORE-0004: Store - Responsive Layout](/Store-Component/STORE-0004_store_responsive_layout.md)
    *   [STORE-0005: Store - Edit Mode](/Store-Component/STORE-0005_store_edit_mode.md)
    *   [STORE-0006: Store - Status Display](/Store-Component/STORE-0006_store_status_display.md)
    *   [STORE-0007: Store - Error Handling](/Store-Component/STORE-0007_store_error_handling.md)
*   [Product Management](/Product-Management)
    *   [PROD-0001: Product - Add Product](/Product-Management/PROD-0001_product_add_product.md)
    *   [PROD-0002: Product - Edit Product](/Product-Management/PROD-0002_product_edit_product.md)
    *   [PROD-0003: Product - Delete Product](/Product-Management/PROD-0003_product_delete_product.md)
    *   [PROD-0004: Product - Price Updates](/Product-Management/PROD-0004_product_price_updates.md)
    *   [PROD-0005: Product - Real-time Updates](/Product-Management/PROD-0005_product_real_time_updates.md)
*   [UI Components](/UI-Components)
    *   [UI-0001: UI - Message Card](/UI-Components/UI-0001_ui_message_card.md)
    *   [UI-0002: UI - Product Card](/UI-Components/UI-0002_ui_product_card.md)
    *   [UI-0003: UI - Search Bar](/UI-Components/UI-0003_ui_search_bar.md)
    *   [UI-0004: UI - Success Dialog](/UI-Components/UI-0004_ui_success_dialog.md)
    *   [UI-0005: UI - Error Display](/UI-Components/UI-0005_ui_error_display.md)
    *   [UI-0006: UI - Store Status Card](/UI-Components/UI-0006_ui_store_status_card.md)
    *   [UI-0007: UI - Animation](/UI-Components/UI-0007_ui_animation.md)
*   [Supabase Integration](/Supabase-Integration)
    *   [SUPA-0001: Supabase - Authentication](/Supabase-Integration/SUPA-0001_supabase_authentication.md)
    *   [SUPA-0002: Supabase - Data Fetching](/Supabase-Integration/SUPA-0002_supabase_data_fetching.md)
    *   [SUPA-0003: Supabase - Real-time Subscriptions](/Supabase-Integration/SUPA-0003_supabase_real_time_subscriptions.md)
    *   [SUPA-0004: Supabase - Error Handling](/Supabase-Integration/SUPA-0004_supabase_error_handling.md)
    *   [SUPA-0005: Supabase - RPC Functions](/Supabase-Integration/SUPA-0005_supabase_rpc_functions.md)
*   [Security Testing](/Security-Testing)
    *   [SEC-0001: Security - Input Validation](/Security-Testing/SEC-0001_security_input_validation.md)
    *   [SEC-0002: Security - XSS Prevention](/Security-Testing/SEC-0002_security_xss_prevention.md)
    *   [SEC-0003: Security - SQL Injection Prevention](/Security-Testing/SEC-0003_security_sql_injection_prevention.md)
    *   [SEC-0004: Security - Authentication Bypass](/Security-Testing/SEC-0004_security_authentication_bypass.md)
    *   [SEC-0005: Security - Content Security Policy](/Security-Testing/SEC-0005_security_content_security_policy.md)
    *   [SEC-0006: Security - CORS Configuration](/Security-Testing/SEC-0006_security_cors_configuration.md)
* 