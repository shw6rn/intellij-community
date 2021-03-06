// Copyright 2000-2018 JetBrains s.r.o. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
package com.intellij.util.ui;

import com.intellij.openapi.util.ScalableIcon;
import com.intellij.testFramework.PlatformTestUtil;
import com.intellij.ui.LayeredIcon;
import com.intellij.ui.RestoreScaleRule;
import org.junit.ClassRule;
import org.junit.Test;
import org.junit.rules.ExternalResource;

import javax.swing.*;

/**
 * Tests {@link com.intellij.ui.LayeredIcon} painting.
 *
 * @author tav
 */
public class LayeredIconPaintTest extends CompositeIconPaintTestHelper {
  @ClassRule
  public static final ExternalResource manageState = new RestoreScaleRule();

  @Test
  @Override
  public void test() {
    super.test();
  }

  @Override
  protected ScalableIcon createCompositeIcon(Icon... cellIcons) {
    LayeredIcon icon = new LayeredIcon(2);
    icon.setIcon(cellIcons[0], 0);
    icon.setIcon(cellIcons[1], 1, JBUI.scale(10), JBUI.scale(6));
    return icon;
  }

  @Override
  protected String getGoldImagePath(int scale) {
    return PlatformTestUtil.getPlatformTestDataPath() + "ui/gold_LayeredIcon@" + scale + "x.png";
  }

  @Override
  protected boolean shouldSaveGoldImage() {
    return false;
  }

  @Override
  protected String[] getCellIconsPaths() {
    return new String[] {
      PlatformTestUtil.getPlatformTestDataPath() + "ui/db_set_breakpoint.png",
      PlatformTestUtil.getPlatformTestDataPath() + "ui/question_badge.png"
    };
  }
}
