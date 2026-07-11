{
  description = "Grokking FP development environment with Scala and Clojure";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Python environment (existing)
            python313
            uv

            # Scala environment
            scala_3
            scalafmt
            sbt
            jdk21

            # Clojure environment
            clojure

            # Optional: metals for IDE support
            metals
          ];

          shellHook = ''
            echo "🎯 Grokking FP Development Environment"
            echo "Python: $(python3 --version 2>&1)"
            echo "Scala: $(scala -version 2>&1)"
            echo "Clojure: $(clojure -Sdescribe | grep ':version' | awk '{print $2}' | tr -d '\"')"
            echo "SBT: $(sbt --version)"
            echo ""
            echo "Python exercises: python src/main/ch01_intro.py"
            echo "Scala REPL: scala"
            echo "Clojure exercises: clojure -M src/other/ch01_intro.clj"
            echo "Create Scala project: sbt new scala/scala3.g8"
          '';
        };
      });
}
