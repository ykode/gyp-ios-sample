{
  'make_global_settings': [
    ['CC', '/usr/bin/clang'],
  ['CXX', '/usr/bin/clang++']
    ],

  'target_defaults': {
    'xcode_settings': {
      'OTHER_CFLAGS': [
        '-fobjc-abi-version=2',
      ],
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'SDKROOT': 'iphoneos',
      'IPHONEOS_DEPLOYMENT_TARGET': '8.2',
      'CODE_SIGN_IDENTITY[sdk=iphoneos*]': 'iPhone Developer',
    }
  },

  'targets': [
    {
      'target_name' : 'HelloGyp',
      'product_name' : 'HelloGyp',
      'type' : 'executable',
      'mac_bundle' : 1,
      'mac_bundle_resources' : [
        'HelloGyp/Base.lproj/LaunchScreen.storyboard',
        'HelloGyp/Base.lproj/Main.storyboard',
        'HelloGyp/Assets.xcassets'
      ],
      'sources': [
        'HelloGyp/AppDelegate.m',
        'HelloGyp/ViewController.m',
        'HelloGyp/main.m'
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
          '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
        ],
      },
      'xcode_settings': {
        'INFOPLIST_FILE': 'HelloGyp/Info.plist',
        'PRODUCT_BUNDLE_IDENTIFIER' : 'io.icemakr.HelloGyp',
        'ASSETCATALOG_COMPILER_APPICON_NAME' : 'AppIcon' 
      }
    }
  ]
}
