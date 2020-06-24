// swift-tools-version:5.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "Atomics",
    products: [
        .library(name: "NIOConcurrencyHelpers", targets: ["NIOConcurrencyHelpers"]),
    ],
    targets: [
        .target(name: "CNIOAtomics"),
        .target(name: "NIOConcurrencyHelpers", dependencies: ["CNIOAtomics"]),
        .testTarget(name: "AtomicsTests", dependencies: []),
    ]
)
