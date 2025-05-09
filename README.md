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
├── Accessibility-Testing/                    # Accessibility Testing Suite  
├── Authentication-Testing/                   # Authentication Testing Suite  
├── Error-Handling/                           # Error Handling Testing Suite  
├── Integration-Testing/                      # Integration Testing Suite     
├── Performance-Testing/                      # Performance Testing Suite     
├── Product-Management/                       # Product Information Manager Testing Suite   
├── Search-Functionality/                     # Search Bar Testing Suite   
├── Security-Testing/                         # Security Testing Suite  
├── Store-Component/                          # Store Component Testing Suite  
├── Supabase-Integration/                     # Supabase Integration Testing Suite  
├── UI-Components/                            # UI Components Testing Suite  
├── User-Management/                          # User Management Testing Suite
├── expand.py                                 # Test Suite Expansion CSV  
├── Project HazelGrove TCM - Test Suites.csv  # Test Suites  
└── README.md                                 # Project Documentation
```

## Test Cases  
 * [Authentication Testing](/Authentication-Testing)  
   * [AUTH-0001: Authentication - Email Validation](/Authentication-Testing/AUTH-0001_authentication_email_validation.md)  
   * [AUTH-0002: Authentication - Password Validation](/Authentication-Testing/AUTH-0002_authentication_password_validation.md)  
   * [AUTH-0003: Authentication - Injection Prevention](/Authentication-Testing/AUTH-0003_authentication_injection_prevention.md)  
   * [AUTH-0004: Authentication - Sign Up Flow](/Authentication-Testing/AUTH-0004_authentication_sign_up_flow.md)  
   * [AUTH-0005: Authentication - Sign In Flow](/Authentication-Testing/AUTH-0005_authentication_sign_in_flow.md)  
   * [AUTH-0006: Authentication - OAuth Integration](/Authentication-Testing/AUTH-0006_authentication_oauth_integration.md)  
   * [AUTH-0007: Authentication - Password Reset](/Authentication-Testing/AUTH-0007_authentication_password_reset.md)  
   * [AUTH-0008: Authentication - Session Management](/Authentication-Testing/AUTH-0008_authentication_session_management.md)  
   * [AUTH-0009: Authentication - CSRF Protection](/Authentication-Testing/AUTH-0009_authentication_csrf_protection.md)  
   * [AUTH-0010: Authentication - Rate Limiting](/Authentication-Testing/AUTH-0010_authentication_rate_limiting.md)  
 * [User Management](/User-Management)  
   * [USER-0001: User Management - Profile Update](/User-Management/USER-0001_user_management_profile_update.md)  
   * [USER-0002: User Management - Role Assignment](/User-Management/USER-0002_user_management_role_assignment.md)  
   * [USER-0003: User Management - User Listing](/User-Management/USER-0003_user_management_user_listing.md)  
   * [USER-0004: User Management - User Filtering](/User-Management/USER-0004_user_management_user_filtering.md)  
   * [USER-0005: User Management - User Deactivation](/User-Management/USER-0005_user_management_user_deactivation.md)  
   * [USER-0006: User Management - User Reactivation](/User-Management/USER-0006_user_management_user_reactivation.md)  
   * [USER-0007: User Management - Permission Checks](/User-Management/USER-0007_user_management_permission_checks.md)  
 * [Search Functionality](/Search-Functionality)  
   * [SEARCH-0001: Search - Product Search](/Search-Functionality/SEARCH-0001_search_product_search.md)  
   * [SEARCH-0002: Search - Store Search](/Search-Functionality/SEARCH-0002_search_store_search.md)  
   * [SEARCH-0003: Search - Combined Search](/Search-Functionality/SEARCH-0003_search_combined_search.md)  
   * [SEARCH-0004: Search - Short Term Handling](/Search-Functionality/SEARCH-0004_search_short_term_handling.md)  
   * [SEARCH-0005: Search - Result Deduplication](/Search-Functionality/SEARCH-0005_search_result_deduplication.md)  
   * [SEARCH-0006: Search - Empty Results Handling](/Search-Functionality/SEARCH-0006_search_empty_results_handling.md)  
   * [SEARCH-0007: Search - Store Selection](/Search-Functionality/SEARCH-0007_search_store_selection.md)  
   * [SEARCH-0008: Search - Performance](/Search-Functionality/SEARCH-0008_search_performance.md)  
   * [SEARCH-0009: Search - Error Handling](/Search-Functionality/SEARCH-0009_search_error_handling.md)  
 * [Store Component](/Store-Component)  
   * [STORE-0001: Store - Data Loading](/Store-Component/STORE-0001_store_data_loading.md)  
   * [STORE-0002: Store - Real-time Updates](/Store-Component/STORE-0002_store_real_time_updates.md)  
   * [STORE-0003: Store - Pagination](/Store-Component/STORE-0003_store_pagination.md)  
   * [STORE-0004: Store - Responsive Layout](/Store-Component/STORE-0004_store_responsive_layout.md)  
   * [STORE-0005: Store - Edit Mode](/Store-Component/STORE-0005_store_edit_mode.md)  
   * [STORE-0006: Store - Status Display](/Store-Component/STORE-0006_store_status_display.md)  
   * [STORE-0007: Store - Error Handling](/Store-Component/STORE-0007_store_error_handling.md)  
 * [Product Management](/Product-Management)  
   * [PROD-0001: Product - Add Product](/Product-Management/PROD-0001_product_add_product.md)  
   * [PROD-0002: Product - Edit Product](/Product-Management/PROD-0002_product_edit_product.md)  
   * [PROD-0003: Product - Delete Product](/Product-Management/PROD-0003_product_delete_product.md)  
   * [PROD-0004: Product - Price Updates](/Product-Management/PROD-0004_product_price_updates.md)  
   * [PROD-0005: Product - Validation](/Product-Management/PROD-0005_product_validation.md)  
   * [PROD-0006: Product - Real-time Updates](/Product-Management/PROD-0006_product_real_time_updates.md)  
   * [PROD-0007: Product - Batch Operations](/Product-Management/PROD-0007_product_batch_operations.md)  
 * [UI Components](/UI-Components)  
   * [UI-0001: UI - Message Card](/UI-Components/UI-0001_ui_message_card.md)  
   * [UI-0002: UI - Product Card](/UI-Components/UI-0002_ui_product_card.md)  
   * [UI-0004: UI - Success Dialog](/UI-Components/UI-0004_ui_success_dialog.md)  
   * [UI-0005: UI - Error Display](/UI-Components/UI-0005_ui_error_display.md)  
   * [UI-0006: UI - Store Status Card](/UI-Components/UI-0006_ui_store_status_card.md)  
   * [UI-0007: UI - Responsive Design](/UI-Components/UI-0007_ui_responsive_design.md)  
   * [UI-0008: UI - Animation](/UI-Components/UI-0008_ui_animation.md)  
 * [Supabase Integration](/Supabase-Integration)  
   * [SUPA-0001: Supabase - Authentication](/Supabase-Integration/SUPA-0001_supabase_authentication.md)  
   * [SUPA-0002: Supabase - Data Fetching](/Supabase-Integration/SUPA-0002_supabase_data_fetching.md)  
   * [SUPA-0003: Supabase - Data Mutations](/Supabase-Integration/SUPA-0003_supabase_data_mutations.md)  
   * [SUPA-0004: Supabase - Real-time Subscriptions](/Supabase-Integration/SUPA-0004_supabase_real_time_subscriptions.md)  
   * [SUPA-0005: Supabase - Error Handling](/Supabase-Integration/SUPA-0005_supabase_error_handling.md)  
   * [SUPA-0007: Supabase - Connection Recovery](/Supabase-Integration/SUPA-0007_supabase_connection_recovery.md)  
 * [Security Testing](/Security-Testing)  
   * [SEC-0001: Security - Input Validation](/Security-Testing/SEC-0001_security_input_validation.md)  
   * [SEC-0002: Security - XSS Prevention](/Security-Testing/SEC-0002_security_xss_prevention.md)  
   * [SEC-0003: Security - SQL Injection Prevention](/Security-Testing/SEC-0003_security_sql_injection_prevention.md)  
   * [SEC-0004: Security - Authentication Bypass](/Security-Testing/SEC-0004_security_authentication_bypass.md)  
   * [SEC-0005: Security - Authorization Checks](/Security-Testing/SEC-0005_security_authorization_checks.md)  
   * [SEC-0006: Security - Sensitive Data Exposure](/Security-Testing/SEC-0006_security_sensitive_data_exposure.md)  
   * [SEC-0007: Security - Content Security Policy](/Security-Testing/SEC-0007_security_content_security_policy.md)  
   * [SEC-0008: Security - CORS Configuration](/Security-Testing/SEC-0008_security_cors_configuration.md)  
   * [SEC-0009: Security - Secure Cookies](/Security-Testing/SEC-0009_security_secure_cookies.md)  
   * [SEC-0010: Security - Error Information Leakage](/Security-Testing/SEC-0010_security_error_information_leakage.md)  
 * [Performance Testing](/Performance-Testing)  
   * [PERF-0001: Performance - Initial Load Time](/Performance-Testing/PERF-0001_performance_initial_load_time.md)  
   * [PERF-0002: Performance - Search Response Time](/Performance-Testing/PERF-0002_performance_search_response_time.md)  
   * [PERF-0003: Performance - Store Load Time](/Performance-Testing/PERF-0003_performance_store_load_time.md)  
   * [PERF-0004: Performance - Animation Performance](/Performance-Testing/PERF-0004_performance_animation_performance.md)  
   * [PERF-0005: Performance - Memory Usage](/Performance-Testing/PERF-0005_performance_memory_usage.md)  
   * [PERF-0006: Performance - Network Efficiency](/Performance-Testing/PERF-0006_performance_network_efficiency.md)  
   * [PERF-0007: Performance - Large Dataset Handling](/Performance-Testing/PERF-0007_performance_large_dataset_handling.md)  
   * [PERF-0008: Performance - Concurrent Operations](/Performance-Testing/PERF-0008_performance_concurrent_operations.md)  
   * [PERF-0009: Performance - Offline Mode](/Performance-Testing/PERF-0009_performance_offline_mode.md)  
   * [PERF-0010: Performance - Low Bandwidth](/Performance-Testing/PERF-0010_performance_low_bandwidth.md)  
 * [Error Handling](/Error-Handling)  
   * [ERR-0001: Error - Network Errors](/Error-Handling/ERR-0001_error_network_errors.md)  
   * [ERR-0002: Error - Authentication Errors](./Error-Handling/ERR-0002_error_authentication_errors.md)  
   * [ERR-0003: Error - Form Validation Errors](/Error-Handling/ERR-0003_error_form_validation_errors.md)  
   * [ERR-0004: Error - API Errors](./Error-Handling/ERR-0004_error_api_errors.md)  
   * [ERR-0005: Error - Supabase Errors](/Error-Handling/ERR-0005_error_supabase_errors.md)  
   * [ERR-0006: Error - Component Errors](/Error-Handling/ERR-0006_error_component_errors.md)  
   * [ERR-0007: Error - Boundary Testing](/Error-Handling/ERR-0007_error_boundary_testing.md)  
 * [Accessibility Testing](/Accessibility-Testing)  
   * [ACC-0001: Accessibility - Keyboard Navigation](/Accessibility-Testing/ACC-0001_accessibility_keyboard_navigation.md)  
   * [ACC-0002: Accessibility - Screen Reader](/Accessibility-Testing/ACC-0002_accessibility_screen_reader.md)  
   * [ACC-0003: Accessibility - Color Contrast](/Accessibility-Testing/ACC-0003_accessibility_color_contrast.md)  
   * [ACC-0004: Accessibility - Text Sizing](/Accessibility-Testing/ACC-0004_accessibility_text_sizing.md)  
   * [ACC-0005: Accessibility - Focus Indicators](/Accessibility-Testing/ACC-0005_accessibility_focus_indicators.md)  
   * [ACC-0006: Accessibility - Form Labels](/Accessibility-Testing/ACC-0006_accessibility_form_labels.md)  
   * [ACC-0007: Accessibility - ARIA Attributes](/Accessibility-Testing/ACC-0007_accessibility_aria_attributes.md)  
 * [Integration Testing](/Integration-Testing)  
   * [INT-0001: Integration - Authentication Flow](/Integration-Testing/INT-0001_integration_authentication_flow.md)  
   * [INT-0002: Integration - Search to Store Flow](/Integration-Testing/INT-0002_integration_search_to_store_flow.md)  
   * [INT-0003: Integration - Product Management Flow](/Integration-Testing/INT-0003_integration_product_management_flow.md)  
   * [INT-0004: Integration - User Management Flow](/Integration-Testing/INT-0004_integration_user_management_flow.md)  
   * [INT-0005: Integration - Error Handling Flow](/Integration-Testing/INT-0005_integration_error_handling_flow.md)  
